from tests import unittest
from iregexp import check

class Quantifiers(unittest.TestCase):

  def test_quantifier(self):
    self.succeed('a*')
    self.succeed('a+')
    self.succeed('a?')
  
  def test_quantity(self):
    self.succeed('a{2}')
    self.succeed('a{2,3}')

  def test_invalid_quantifiers(self):
    self.fail('*')
    self.fail('+')
    self.fail('?')
    self.fail('a**')
    self.fail('a++')
    self.fail('a??')

  def test_invalid_quantity(self):
    self.fail('{')
    self.fail('}')
    self.fail('{}')
    self.fail('{,}')
    self.fail('{4,}')
    self.fail('{,2}')
    self.fail('a{')
    self.fail('a}')
    self.fail('a{}')
    self.fail('a{,}')
    self.fail('a{4,}')
    self.fail('a{,2}')

  ## TODO:
  ##it('should self.fail on incorrect quantity', () => {
  ##def test_incorrect_quantity(self):
  ##  self.self.fail(',,{5,3}')

  def succeed(self, expression):
    self.assertTrue(check(expression)[0])
  def fail(self, expression):
    self.assertFalse(check(expression)[0])