from tests import unittest
from iregexp import check

class SomeTests(unittest.TestCase):

  def test_sample(self):
    self.succeed('[aeiouy]*')

  def succeed(self, expression):
    self.assertTrue(check(expression)[0])
