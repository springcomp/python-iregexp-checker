from tests import unittest
from iregexp import check

class NormalChar(unittest.TestCase):

  def test_00_27(self):
    self.succeed('\u0000')
    self.succeed('\u0001')
    self.succeed('\u0002')
    self.succeed('\u0003')
    self.succeed('\u0004')
    self.succeed('\u0005')
    self.succeed('\u0006')
    self.succeed('\u0007')
    self.succeed('\u0008')
    self.succeed('\u0009')
    self.succeed('\u000a')
    self.succeed('\u000b')
    self.succeed('\u000c')
    self.succeed('\u000d')
    self.succeed('\u000e')
    self.succeed('\u000f')
    self.succeed('\u0010')
    self.succeed('\u0011')
    self.succeed('\u0012')
    self.succeed('\u0013')
    self.succeed('\u0014')
    self.succeed('\u0015')
    self.succeed('\u0016')
    self.succeed('\u0017')
    self.succeed('\u0018')
    self.succeed('\u0019')
    self.succeed('\u001a')
    self.succeed('\u001b')
    self.succeed('\u001c')
    self.succeed('\u001d')
    self.succeed('\u001e')
    self.succeed('\u001f')
    self.succeed('\u0020')
    self.succeed('\u0021')
    self.succeed('\u0022')
    self.succeed('\u0023')
    self.succeed('\u0024')
    self.succeed('\u0025')
    self.succeed('\u0026')
    self.succeed('\u0027')

  def test_2F_3E(self):
    self.succeed('\u002f')
    self.succeed('\u0030')
    self.succeed('\u0031')
    self.succeed('\u0032')
    self.succeed('\u0033')
    self.succeed('\u0034')
    self.succeed('\u0035')
    self.succeed('\u0036')
    self.succeed('\u0037')
    self.succeed('\u0038')
    self.succeed('\u0039')
    self.succeed('\u003a')
    self.succeed('\u003b')
    self.succeed('\u003c')
    self.succeed('\u003d')
    self.succeed('\u003e')
  
  def test_40_5A(self):
    self.succeed('\u0040')
    self.succeed('\u0041')
    self.succeed('\u0042')
    self.succeed('\u0043')
    self.succeed('\u0044')
    self.succeed('\u0045')
    self.succeed('\u0046')
    self.succeed('\u0047')
    self.succeed('\u0048')
    self.succeed('\u0049')
    self.succeed('\u004a')
    self.succeed('\u004b')
    self.succeed('\u004c')
    self.succeed('\u004d')
    self.succeed('\u004e')
    self.succeed('\u004f')
    self.succeed('\u0050')
    self.succeed('\u0051')
    self.succeed('\u0052')
    self.succeed('\u0053')
    self.succeed('\u0054')
    self.succeed('\u0055')
    self.succeed('\u0056')
    self.succeed('\u0057')
    self.succeed('\u0058')
    self.succeed('\u0059')
    self.succeed('\u005a')
  
  def test_5E_7A(self):
    self.succeed('\u005e')
    self.succeed('\u005f')
    self.succeed('\u0060')
    self.succeed('\u0061')
    self.succeed('\u0062')
    self.succeed('\u0063')
    self.succeed('\u0064')
    self.succeed('\u0065')
    self.succeed('\u0066')
    self.succeed('\u0067')
    self.succeed('\u0068')
    self.succeed('\u0069')
    self.succeed('\u006a')
    self.succeed('\u006b')
    self.succeed('\u006c')
    self.succeed('\u006d')
    self.succeed('\u006e')
    self.succeed('\u006f')
    self.succeed('\u0070')
    self.succeed('\u0071')
    self.succeed('\u0072')
    self.succeed('\u0073')
    self.succeed('\u0074')
    self.succeed('\u0075')
    self.succeed('\u0076')
    self.succeed('\u0077')
    self.succeed('\u0078')
    self.succeed('\u0079')
    self.succeed('\u007a')
  
  def test_7E_10FFF(self):
    self.succeed('\u007e')
    self.succeed('\u007f')
    self.succeed('\u0080')
    self.succeed('\u0081')
    ## ...

  def test_miscellaneous(self):
    self.succeed(',,')

  def succeed(self, expression):
    self.assertTrue(check(expression))
  def fail(self, expression):
    self.assertFalse(check(expression))