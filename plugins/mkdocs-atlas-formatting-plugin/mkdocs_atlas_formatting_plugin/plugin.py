from typing import Optional

from mkdocs.config.base import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

from .atlaswebserver import AtlasWebServer
from .logconfig import setup_logging
from .parser import Parser

logger = setup_logging(__name__)


class AtlasFormattingPlugin(BasePlugin):
    webserver: Optional[AtlasWebServer] = None

    def on_pre_build(self, config: Config) -> None:
        logger.info('pre-build')
        self.webserver = AtlasWebServer()

    def on_page_content(self, html: str, page: Page, config: Config, files: Files) -> str:
        parser = Parser(page.title, html)
        return parser.html
