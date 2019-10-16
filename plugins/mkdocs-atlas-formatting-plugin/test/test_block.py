import unittest

from mkdocs_atlas_formatting_plugin.atlaswebserver import NoopWebserver
from mkdocs_atlas_formatting_plugin.block import Block
from mkdocs_atlas_formatting_plugin.logconfig import setup_logging

from .resources import *

logger = setup_logging(__name__)


class BlockTest(unittest.TestCase):

    def validate_empty_block(self, block: Block):
        self.assertEqual(None, block.type)
        self.assertEqual(None, block.options)
        self.assertEqual(False, block.is_started)
        self.assertEqual(None, block.input_lines)

    def test_parse_options_single(self):
        block = Block(NoopWebserver())
        block.parse_options(options_single)

        self.assertEqual({'show-expr': 'true'}, block.options)

        block.complete()

        self.validate_empty_block(block)

    def test_parse_options_multiple(self):
        block = Block(NoopWebserver())
        block.parse_options(options_multiple)

        self.assertEqual({'show-expr': 'true', 'something-else': 'false'}, block.options)

        block.complete()

        self.validate_empty_block(block)

    def test_parse_options_no_equals(self):
        block = Block(NoopWebserver())
        block.parse_options(options_no_equals)

        self.assertEqual(None, block.options)

        block.complete()

        self.validate_empty_block(block)

    def test_parse_options_unencoded_equals(self):
        block = Block(NoopWebserver())
        block.parse_options(options_unencoded_equals)

        self.assertEqual(None, block.options)

        block.complete()

        self.validate_empty_block(block)

    def test_parse_options_encoded_equals(self):
        block = Block(NoopWebserver())
        block.parse_options(options_encoded_equals)

        self.assertEqual({'hilite': '&l=0', 'something-else': '&l=0'}, block.options)

        block.complete()

        self.validate_empty_block(block)

    def test_query_pattern(self):
        for uri in block_query_patterns:
            m = Block.query_pattern.match(uri)
            self.assertEqual('nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum', m.group(1))

    def test_mk_image_tag(self):
        block = Block(NoopWebserver())
        image_tag = block.mk_image_tag(atlas_graph_line)

        data_uri = f'data:image/png;base64,{NoopWebserver.ENCODED}'
        width = NoopWebserver.WIDTH
        height = NoopWebserver.HEIGHT

        self.assertEqual(f'<img src="{data_uri}" width="{width}" height="{height}"/>', image_tag)

        block.complete()

        self.validate_empty_block(block)

    def test_mk_asl_link(self):
        block = Block(NoopWebserver())
        asl_link = block.mk_asl_link(':eq')

        self.assertEqual(f'<a href="{block.ASL_BASE_URI}/eq/">:eq</a>', asl_link)

        block.complete()

        self.validate_empty_block(block)

    def test_fmt_atlas_expr(self):
        block = Block(NoopWebserver())
        formatted = block.fmt_atlas_expr(atlas_graph_line)

        self.assertEqual(True, formatted.startswith('nf.app,alerttest,'))
        self.assertEqual(True, formatted.endswith(':sum</a>\n'))
        self.assertEqual(False, formatted.endswith(':sum,</a>\n'))
        self.assertEqual(4, formatted.count('\n'))
        self.assertEqual(4, formatted.count('<a href='))

        block.complete()

        self.validate_empty_block(block)

    def test_mk_table_row(self):
        block = Block(NoopWebserver())
        table_row = block.mk_table_row(['a', 'b', 'c'])

        self.assertEqual(True, table_row.startswith('<tr>'))
        self.assertEqual(True, table_row.endswith('</tr>'))
        self.assertEqual(3, table_row.count('<td>'))
        self.assertEqual(3, table_row.count('</td>'))

        block.complete()

        self.validate_empty_block(block)

    def test_hilite(self):
        block = Block(NoopWebserver())
        output = block.hilite('bar baz foo', 'baz')

        self.assertEqual('bar <span class="atlas-hilite">baz</span> foo', output)

        block.complete()

        self.validate_empty_block(block)

    def test_atlas_example_block(self):
        block = Block(NoopWebserver())
        block.start('Atlas Example Block Start', atlas_example_start_line)

        self.assertEqual(Block.ATLAS_EXAMPLE, block.type)
        self.assertEqual(None, block.options)
        self.assertEqual(True, block.is_started)
        self.assertEqual(None, block.input_lines)

        block.add_line(atlas_example_line)

        self.assertEqual(1, len(block.input_lines))
        self.assertEqual(2, len(block.input_lines[0]))
        self.assertEqual(15, len(block.input_lines[0][0]))
        self.assertEqual(132, len(block.input_lines[0][1]))
        self.assertEqual('Dampened Signal', block.input_lines[0][0])
        self.assertEqual(True, block.input_lines[0][1].startswith('/api/v1/graph'))

        block.build_output()

        self.assertEqual(5, len(block.output_lines))
        self.assertEqual(14, len(block.output_lines[0]))
        self.assertEqual(True, block.output_lines[0].startswith('<table>'))

        block.complete()

        self.validate_empty_block(block)

    def test_atlas_graph_block(self):
        block = Block(NoopWebserver())
        block.start('Atlas Graph Block Start', atlas_graph_start_line)

        self.assertEqual(Block.ATLAS_GRAPH, block.type)
        self.assertEqual({'show-expr': 'true'}, block.options)
        self.assertEqual(True, block.is_started)
        self.assertEqual(None, block.input_lines)
        self.assertEqual(None, block.output_lines)

        block.add_line(atlas_graph_line)

        self.assertEqual(1, len(block.input_lines))
        self.assertEqual(108, len(block.input_lines[0]))
        self.assertEqual(True, block.input_lines[0].startswith('/api/v1/graph'))

        block.build_output()

        self.assertEqual(2, len(block.output_lines))
        self.assertEqual(169, len(block.output_lines[0]))
        self.assertEqual(True, block.output_lines[0].startswith('<p><img src='))
        self.assertEqual(True, block.output_lines[1].startswith('<pre>'))

        block.complete()

        self.validate_empty_block(block)

    def test_atlas_stacklang_block(self):
        block = Block(NoopWebserver())
        block.start('Atlas StackLang Block Start', atlas_stacklang_start_line)

        self.assertEqual(Block.ATLAS_STACKLANG, block.type)
        self.assertEqual(None, block.options)
        self.assertEqual(True, block.is_started)
        self.assertEqual(None, block.input_lines)
        self.assertEqual(None, block.output_lines)

        block.add_line(atlas_stacklang_line)

        self.assertEqual(1, len(block.input_lines))
        self.assertEqual(108, len(block.input_lines[0]))
        self.assertEqual(True, block.input_lines[0].startswith('/api/v1/graph'))

        block.build_output()

        self.assertEqual(1, len(block.output_lines))
        self.assertEqual(318, len(block.output_lines[0]))
        self.assertEqual(True, block.output_lines[0].startswith('<pre>'))

        block.complete()

        self.validate_empty_block(block)

    def test_atlas_uri_block(self):
        block = Block(NoopWebserver())
        block.start('Atlas URI Block Start', atlas_uri_start_line)

        self.assertEqual(Block.ATLAS_URI, block.type)
        self.assertEqual(None, block.options)
        self.assertEqual(True, block.is_started)
        self.assertEqual(None, block.input_lines)
        self.assertEqual(None, block.output_lines)

        block.add_line(atlas_uri_line)

        self.assertEqual(1, len(block.input_lines))
        self.assertEqual(108, len(block.input_lines[0]))
        self.assertEqual(True, block.input_lines[0].startswith('/api/v1/graph'))

        block.build_output()

        self.assertEqual(1, len(block.output_lines))
        self.assertEqual(412, len(block.output_lines[0]))
        self.assertEqual(True, block.output_lines[0].startswith('<pre>'))

        block.complete()

        self.validate_empty_block(block)

    def test_invalid_block(self):
        block = Block(NoopWebserver())
        block.start('Invalid Block Start', invalid_start_line)
        block.add_line(atlas_graph_line)

        self.validate_empty_block(block)
