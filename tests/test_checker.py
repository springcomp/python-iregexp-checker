from tests import unittest
from iregexp import check

class Checker(unittest.TestCase):

  def test_checker(self):
    with self.assertRaises(Exception):
      check('[?', False)
