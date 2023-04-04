from tests import unittest
from iregexp import check

class Branch(unittest.TestCase):

  def test_branch(self):
    self.succeed('a|b')
    self.succeed('a|')

  def test_invalid_branch(self):
    self.fail('|')
    self.fail('||')
    self.fail('|?')

  def succeed(self, expression):
    self.assertTrue(check(expression)[0])
  def fail(self, expression):
    self.assertFalse(check(expression)[0])