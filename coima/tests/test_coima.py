from unittest import TestCase
from coima import Template


class TestCoima(TestCase):

    def test_simple_render(self):
        replace = {'port':'8080', 'host':'localhost'}
        t = Template(replace, 'foo.conf')
        result = t.render()
        expected = '# Simple Configuration File for Testing\n#\nport = 8080\nhost = localhost\n\n\n'
        self.assertEqual(result, expected)

    def test_no_render(self):
        t = Template({}, 'foo.conf')
        result = t.render()
        expected = '# Simple Configuration File for Testing\n#\nport = {{port}}\nhost = {{host}}\n\n\n'
        self.assertEqual(result, expected)

