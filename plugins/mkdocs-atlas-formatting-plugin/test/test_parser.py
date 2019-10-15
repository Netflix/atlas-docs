import unittest

from .resources import alerting_expressions
from mkdocs_atlas_formatting_plugin.atlaswebserver import NoopWebserver
from mkdocs_atlas_formatting_plugin.logconfig import setup_logging
from mkdocs_atlas_formatting_plugin.parser import Parser

logger = setup_logging(__name__)


class ParserTest(unittest.TestCase):

    def test_input_length(self):
        split = alerting_expressions.split('\n')

        self.assertEqual(3471, len(alerting_expressions))
        self.assertEqual(45, len(split))

    def test_parser(self):
        parser = Parser('Alerting Expressions', alerting_expressions, NoopWebserver())

        self.assertEqual(4, parser.block_count)
