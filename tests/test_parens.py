from tests import unittest
from iregexp import check

class Parens(unittest.TestCase):

  def test_parens(self):
    self.succeed('(a)')
    self.succeed('(a)+')
    self.succeed('(a){2}')
    self.succeed('(a){2,3}')

  def test_sequence(self):
    self.succeed('a(a)a')

  def test_mismatched(self):
    self.fail('(')
    self.fail(')')
    self.fail('(a')
    self.fail('a)')

  def succeed(self, expression):
    self.assertTrue(check(expression))
  def fail(self, expression):
    self.assertFalse(check(expression))