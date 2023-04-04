from tests import unittest
from iregexp import ensureExpression

class Checker(unittest.TestCase):

  def test_checker(self):
    with self.assertRaises(Exception):
      ensureExpression('[?')
