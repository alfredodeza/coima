from mock import MockSys
import sys
from unittest import TestCase
from coima import Template


class TestCoima(TestCase):

    def test_simple_render(self):
        replace = {'port':'8080', 'host':'localhost'}
        t = Template(replace, 'foo.conf')
        sys.stdout = MockSys()
        t.render()
        result = sys.stdout.captured()
        expected = '# Simple Configuration File for Testing\n#\nport = 8080\nhost = localhost\n\n\n\n'
        self.assertEqual(result, expected)


