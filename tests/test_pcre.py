from tests import unittest
from iregexp import toPCRE

class PCRE(unittest.TestCase):

  def test_PCRE(self):
    self.assertMapsTo('a', False, 'a')
    self.assertMapsTo('\\.', False, '\\.')
    self.assertMapsTo('\\.\\\\.', False, '\\.\\\\[^\\\\n\\\\r]')
    self.assertMapsTo('[a-z.+]', False, '[a-z.+]')

  def test_PCRE_anchored(self):
    self.assertMapsTo('a', True, '\\A(?:a)\\Z')
    self.assertMapsTo('\\.', True, '\\A(?:\\.)\Z')
    self.assertMapsTo('\\.\\\\.', True, '\\A(?:\\.\\\\[^\\\\n\\\\r])\Z')
    self.assertMapsTo('[a-z.+]', True, '\\A(?:[a-z.+])\Z')

  def assertMapsTo(self, expression, anchor, expected):
    self.assertEqual(toPCRE(expression, anchor), expected)