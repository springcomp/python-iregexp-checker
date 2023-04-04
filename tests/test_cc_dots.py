from tests import unittest
from iregexp import check

class Dot(unittest.TestCase):

  def test_dot(self):
    self.succeed('.')
    self.succeed('..')
    self.succeed('.*')
    self.succeed('.?')

  def succeed(self, expression):
    self.assertTrue(check(expression))
  def fail(self, expression):
    self.assertFalse(check(expression))