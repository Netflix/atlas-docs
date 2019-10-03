from typing import List, Optional

from .atlaswebserver import NoopWebserver
from .block import Block
from .logconfig import setup_logging

logger = setup_logging(__name__)


class Parser:
    def __init__(self, page_title: str, html: str, webserver: Optional[NoopWebserver] = None):
        self.webserver = webserver

        self.page_title: str = page_title
        self.block_count: int = 0
        self.input_lines: List[str] = html.split('\n')
        self.output_lines: List[str] = []
        self.html: Optional[str] = None
        self.tokenize()

    def tokenize(self) -> None:
        block = Block() if not self.webserver else Block(self.webserver)

        for in_line in self.input_lines:
            if not block.is_started and self.block_start(in_line):
                block.start(self.page_title, in_line)
            elif block.is_started and self.block_end(in_line):
                block.build_output()
                for out_line in block.output_lines:
                    self.output_lines.append(out_line)
                self.block_count += 1
                block.complete()
            elif block.is_started:
                block.add_line(in_line.replace('&amp;', '&'))
            else:
                self.output_lines.append(in_line)

        self.html = '\n'.join(self.output_lines)

    @staticmethod
    def block_start(line: str) -> bool:
        return line.startswith('<p>@@@')

    @staticmethod
    def block_end(line: str) -> bool:
        return line.startswith('@@@</p>')
