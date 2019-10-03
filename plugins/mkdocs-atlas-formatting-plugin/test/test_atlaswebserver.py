import os
import unittest
from typing import Optional

from .resources import atlas_graph_line, graph_image_html_template
from mkdocs_atlas_formatting_plugin.atlaswebserver import AtlasWebServer
from mkdocs_atlas_formatting_plugin.logconfig import setup_logging

logger = setup_logging(__name__)


class AtlasWebServerTest(unittest.TestCase):
    webserver: Optional[AtlasWebServer] = None
    dirname: str = os.path.dirname(os.path.realpath(__file__))

    def setUp(self) -> None:
        self.webserver = AtlasWebServer()

    def test_get_image(self):
        fname = f'{self.dirname}/test_atlaswebserver.html'
        data_uri, width, height = self.webserver.get_image(atlas_graph_line)

        logger.info(f'save image as {fname}')

        with open(fname, 'w') as f:
            output = graph_image_html_template\
                .replace('IMG_SRC', data_uri)\
                .replace('IMG_WIDTH', str(width))\
                .replace('IMG_HEIGHT', str(height))

            f.write(output)

        self.assertEqual(17718, len(data_uri))
        self.assertEqual(786, width)
        self.assertEqual(221, height)

    def tearDown(self) -> None:
        self.webserver.shutdown()
