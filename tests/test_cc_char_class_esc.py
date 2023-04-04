from tests import unittest
from iregexp import check

class CharClassEsc(unittest.TestCase):

  def test_pC_Others(self):
    self.succeed('\\p{C}')
    self.succeed('\\p{Cc}')
    self.succeed('\\p{Cf}')
    self.succeed('\\p{Cn}')
    self.succeed('\\p{Co}')
  
  def test_invalid_pC(self):
    self.fail('\\p{Cx}')

  def test_pL_Letters(self):
    self.succeed('\\p{L}')
    self.succeed('\\p{Ll}')
    self.succeed('\\p{Lm}')
    self.succeed('\\p{Lo}')
    self.succeed('\\p{Lt}')
    self.succeed('\\p{Lu}')

  def test_invalid_pL(self):
    self.fail('\\p{Lx}')

  def test_pM_Marks(self):
    self.succeed('\\p{M}')
    self.succeed('\\p{Mc}')
    self.succeed('\\p{Me}')
    self.succeed('\\p{Mn}')

  def test_invalid_pM(self):
    self.fail('\\p{Mx}')

  def test_pN_Numbers(self):
    self.succeed('\\p{N}')
    self.succeed('\\p{Nd}')
    self.succeed('\\p{Nl}')
    self.succeed('\\p{No}')

  def test_invalid_pN(self):
    self.fail('\\p{Nx}')

  def test_pP_Punctuation(self):
    self.succeed('\\p{P}')
    self.succeed('\\p{Pc}')
    self.succeed('\\p{Pd}')
    self.succeed('\\p{Pe}')
    self.succeed('\\p{Pf}')
    self.succeed('\\p{Pi}')
    self.succeed('\\p{Po}')
    self.succeed('\\p{Ps}')

  def test_invalid_pP(self):
    self.fail('\\p{Px}')

  def test_pZ_Separators(self):
    self.succeed('\\p{Z}')
    self.succeed('\\p{Zl}')
    self.succeed('\\p{Zp}')
    self.succeed('\\p{Zs}')

  def test_invalid_pZ(self):
    self.fail('\\p{Zx}')

  def test_pS_Letters(self):
    self.succeed('\\p{S}')
    self.succeed('\\p{Sc}')
    self.succeed('\\p{Sk}')
    self.succeed('\\p{Sm}')
    self.succeed('\\p{So}')

  def test_invalid_pS(self):
    self.fail('\\p{Sx}')

  def test_pIs_IsBlock(self):
    self.succeed('\\p{IsAlpha}')
    self.succeed('\\p{IsLatin}')

  def test_pIs_IsBlock_Syntax(self):
    self.succeed('\\p{Is-0123-abcd-456-ABCD-789-EFGH-}')

  def test_invalid_pIs(self):
    self.fail('\\p{Is}')

  def test_character_prop_in_range(self):
    self.succeed('[\\p{L}]')
    self.succeed('[\\p{M}]')
    self.succeed('[\\p{Lo}\\p{Me}]')

  def test_invalid_p_charProp(self):
    self.fail('\\p')
    self.fail('\\p{')
    self.fail('\\p{}')

  def succeed(self, expression):
    self.assertTrue(check(expression))
  def fail(self, expression):
    self.assertFalse(check(expression))