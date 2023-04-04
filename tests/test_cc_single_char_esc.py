from tests import unittest
from iregexp import check

class SingleCharEsc(unittest.TestCase):

  def test_28_2B(self):
    self.succeed('[\\(]')
    self.succeed('[\\)]')
    self.succeed('[\\*]')
    self.succeed('[\\+]')

  def test_2D_2E(self):
    self.succeed('[\\-]')
    self.succeed('[\\\\]')

  def test_question_mark(self):
    self.succeed('[\\?]')

  def test_5B_5E(self):
    self.succeed('[\\?]')

    self.succeed('[\\[]')
    self.succeed('[\\\\]')
    self.succeed('[\\]]')
    self.succeed('[\\^]')

  def test_n_r_t(self):
    self.succeed('[\\n]')
    self.succeed('[\\r]')
    self.succeed('[\\t]')

  def test_7B_7D(self):
    self.succeed('[\\{]')
    self.succeed('[\\|]')
    self.succeed('[\\}]')

  def test_sequence(self):
    self.succeed('[\\(\\*\\+\\)]')
    self.succeed('[\\(\\-\\\\\\)]')
    self.succeed('[\\(\\?\\)]')
    self.succeed('[\\n\\r\\t]')

  def test_invalid_escape(self):
    self.fail('[\\a]')
    self.fail('[\\0]')
    self.fail('[\\,]')

  def succeed(self, expression):
    self.assertTrue(check(expression))
  def fail(self, expression):
    self.assertFalse(check(expression))