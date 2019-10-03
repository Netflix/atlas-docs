import re
from typing import Dict, List, Optional, Tuple, Union

from .logconfig import setup_logging
from .atlaswebserver import AtlasWebServer, NoopWebserver

logger = setup_logging(__name__)


class Block:
    ASL_BASE_URI = 'https://netflix.github.io/atlas-docs/asl/ref'

    ATLAS_EXAMPLE = 'atlas-example'
    ATLAS_GRAPH = 'atlas-graph'
    ATLAS_STACKLANG = 'atlas-stacklang'

    valid_types = [
        ATLAS_EXAMPLE,
        ATLAS_GRAPH,
        ATLAS_STACKLANG
    ]

    example_pattern = re.compile('([^:]+): (.+)')
    options_pattern = re.compile('.+@@@ ([a-z\\-]+)(?:$| { (.+) })')
    query_pattern = re.compile('.*q=(.+)')

    def __init__(self, webserver: Optional[NoopWebserver] = None) -> None:
        self.webserver: AtlasWebServer = AtlasWebServer() if not webserver else webserver

        self.type: Optional[str] = None
        self.options: Optional[Dict[str, str]] = None
        self.is_started: bool = False
        self.input_lines: Optional[Union[List[str], List[Tuple[str, str]]]] = None
        self.output_lines: Optional[List[str]] = None

    def start(self, page_title: str, line: str) -> None:
        m = self.options_pattern.match(line)

        if not m:
            return

        block_type = m.group(1)
        block_options = m.group(2)

        if block_type in self.valid_types:
            self.type = block_type
            self.options = self.parse_options(block_options)
            self.is_started = True
        else:
            logger.warning(f'invalid block type `{block_type}` on page `{page_title}`')

    @staticmethod
    def parse_options(options: Optional[str]) -> Optional[Dict[str, str]]:
        if options:
            res = {}

            for option in options.split(' '):
                if '=' not in option:
                    continue
                k, v = option.split('=')
                res[k] = v

            return res

    def complete(self) -> None:
        self.type = None
        self.options = None
        self.is_started = False
        self.input_lines = None
        self.output_lines = None

    def add_line(self, line: str) -> None:
        if not self.is_started:
            return

        if self.type == self.ATLAS_EXAMPLE:
            m = self.example_pattern.match(line)

            if m:
                line = m.groups()

        if self.input_lines is None:
            self.input_lines = [line]
        else:
            self.input_lines.append(line)

    def mk_image_tag(self, uri: str) -> str:
        """
        Given an Atlas URI, fetch the image from a running Atlas Standalone server and format
        the output as an image tag, suitable for embedding in an HTML page.

        Input:

        /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt

        Output:

        <img src="data:image/png;base64,...encoded image..." width="286" height="153">
        """

        data_uri, width, height = self.webserver.get_image(uri)
        return f'<img src="{data_uri}" width="{width}" height="{height}"/>'

    def mk_asl_link(self, op: str) -> str:
        stripped_op = op.replace(":", "")
        return f'<a href="{self.ASL_BASE_URI}/{stripped_op}/">{op}</a>'

    def fmt_atlas_expr(self, uri: str) -> str:
        """
        Given an Atlas URI, extract the query and convert it into a pre-formatted block.

        There should be line breaks after each operator and each operator should link to the
        Atlas Stack Language Reference.

        Input:

        /api/v1/graph?w=200&h=150&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt,5,:rolling-count

        Output:

        <pre>nf.app,alerttest,<a href="https://netflix.github.io/atlas-docs/asl/ref/eq/">:eq</a>,
        name,ssCpuUser,<a href="https://netflix.github.io/atlas-docs/asl/ref/eq/">:eq</a>,
        <a href="https://netflix.github.io/atlas-docs/asl/ref/and/">:and</a>,
        <a href="https://netflix.github.io/atlas-docs/asl/ref/sum/">:sum</a>,
        80,<a href="https://netflix.github.io/atlas-docs/asl/ref/gt/">:gt</a>,
        5,<a href="https://netflix.github.io/atlas-docs/asl/ref/rolling-count/">:rolling-count</a></pre>
        """

        m = self.query_pattern.match(uri)

        if not m:
            return '<pre>ERROR: query not found</pre>'

        line = ''
        output_lines = []

        for item in m.group(1).split(','):
            if item.startswith(':'):
                output_lines.append(f'{line}{self.mk_asl_link(item)},')
                line = ''
            else:
                line += f'{item},'

        output_lines[-1] = output_lines[-1][:-1]  # strip trailing comma
        atlas_expr = '\n'.join(output_lines)

        return f'<pre>{atlas_expr}</pre>'

    @staticmethod
    def mk_table_row(data: List[str]) -> str:
        out_line = ''.join([f'<td>{item}</td>' for item in data])
        return f'<tr>{out_line}</tr>'

    def build_output(self) -> None:
        method_name = 'build_' + self.type.replace('-', '_')

        try:
            getattr(self, method_name)()
        except AttributeError:
            logger.error(f'{method_name} method is missing')

    def build_atlas_example(self) -> None:
        titles, graphs, exprs = [], [], []

        for title, uri in self.input_lines:
            titles.append(title)
            graphs.append(self.mk_image_tag(uri))
            exprs.append(self.fmt_atlas_expr(uri))

        self.output_lines = ['<table><tbody>']
        self.output_lines.append(self.mk_table_row(titles))
        self.output_lines.append(self.mk_table_row(graphs))
        self.output_lines.append(self.mk_table_row(exprs))
        self.output_lines.append('</tbody></table>')

    def build_atlas_graph(self) -> None:
        uri = self.input_lines[0]
        self.output_lines = [f'<p>{self.mk_image_tag(uri)}</p>']

        if self.options['show-expr'] == 'true':
            self.output_lines.append(self.fmt_atlas_expr(uri))

    def build_atlas_stacklang(self):
        self.output_lines = [self.fmt_atlas_expr(self.input_lines[0])]
