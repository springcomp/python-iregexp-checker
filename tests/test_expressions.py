from tests import unittest
from iregexp import check

class AppendixA(unittest.TestCase):

  def test_rfc6021_txt__631(self):
    self.succeed('([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?')
  def test_rfc6021_txt__647(self):
    self.succeed('[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}')
  def test_rfc6021_txt__933(self):
    self.succeed('((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}')
  def test_rfc6021_txt__938(self):
    self.succeed('(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|')
  def test_rfc6991_txt_1169(self):
    self.succeed('(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|')
  def test_rfc6021_txt_1031(self):
    self.succeed('(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|')
  def test_rfc6991_txt_1046(self):
    self.succeed('(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|')
  def test_rfc6021_txt_1026(self):
    self.succeed('((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}')
  def test_rfc6020_txt_6647(self):
    self.succeed('[0-9a-fA-F]*')
  def test_rfc6110_txt_1583(self):
    self.succeed('[aeiouy]*')
  def test_rfc6110_txt_3222(self):
    self.succeed('[A-Z][a-z]*')
  def test_rfc6536_txt_1583(self):
    self.succeed('\\*')
  def test_rfc6536_txt_1632(self):
    self.succeed('[^\\*].*')
  def test_rfc6643_txt__524(self):
    self.succeed('\\p{IsBasicLatin}{0,255}')

  def test_rfc6991_txt__541(self):
    self.succeed('[a-zA-Z_][a-zA-Z0-9\\-_.]*')
  def test_rfc6991_txt__542(self):
    self.succeed('.|..|[^xX].*|.[^mM].*|..[^lL].*')
  def test_rfc6991_txt__665(self):
    self.succeed('([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?')
  def test_rfc6991_txt__693(self):
    self.succeed('[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}')
  def test_rfc6991_txt__725(self):
    self.succeed('([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?')
  def test_rfc6991_txt__743(self):
    self.succeed('[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-')
  def test_rfc6991_txt_1041(self):
    self.succeed('((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}')
  def test_rfc6991_txt_1099(self):
    self.succeed('[0-9\\.]*')
  def test_rfc6991_txt_1109(self):
    self.succeed('[0-9a-fA-F:\\.]*')
  def test_rfc6991_txt_1164(self):
    self.succeed('((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}')
  def test_rfc7407_txt__933(self):
    self.succeed('([0-9a-fA-F]){2}(:([0-9a-fA-F]){2}){0,254}')
  def test_rfc7407_txt_1494(self):
    self.succeed('([0-9a-fA-F]){2}(:([0-9a-fA-F]){2}){4,31}')
  def test_rfc7950_txt_8323(self):
    self.succeed('[0-9a-fA-F]*')
  def test_rfc7950_txt_8355(self):
    self.succeed('[a-zA-Z_][a-zA-Z0-9\\-_.]*')
  def test_rfc7950_txt_8356(self):
    self.succeed('[xX][mM][lL].*')
  def test_rfc8049_txt_6704(self):
    self.succeed('[A-Z]{2}')
  def test_rfc8194_txt__629(self):
    self.succeed('\\*')
  def test_rfc8194_txt__637(self):
    self.succeed('[0-9]{8}\\.[0-9]{6}')
  def test_rfc8194_txt__963(self):
    self.succeed('(2((2[4-9])|(3[0-9]))\\.).*')
  def test_rfc8194_txt__974(self):
    self.succeed('(([fF]{2}[0-9a-fA-F]{2}):).*')
  def test_rfc8299_txt_7986(self):
    self.succeed('[A-Z]{2}')
  def test_rfc8341_txt_1878(self):
    self.succeed('\\*')
  def test_rfc8341_txt_1927(self):
    self.succeed('[^\\*].*')
  def test_rfc8407_txt_1723(self):
    self.succeed('[0-9\\.]*')
  def test_rfc8407_txt_1749(self):
    self.succeed('[a-zA-Z_][a-zA-Z0-9\\-_.]*')
  def test_rfc8407_txt_1750(self):
    self.succeed('.|..|[^xX].*|.[^mM].*|..[^lL].*')
  def test_rfc8776_txt__838(self):
    self.succeed('/?([a-zA-Z0-9\\-_.]+)(/[a-zA-Z0-9\\-_.]+)*')
  def test_rfc8776_txt__874(self):
    self.succeed('([a-zA-Z0-9\\-_.]+:)*')
  def test_rfc8944_txt__596(self):
    self.succeed('[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){7}')

  def test_rfc6095_txt_2544(self):
    self.fail('\\S(.*\\S)?')
  def test_rfc6021_txt__459(self):
    self.fail('(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))')
  def test_rfc6021_txt__513(self):
    self.fail('\\d*(\\.\\d*){1,127}')
  def test_rfc6021_txt__529(self):
    self.fail('\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?')
  def test_rfc6728_txt_3480(self):
    self.fail('\\S+')
  def test_rfc6728_txt_3500(self):
    self.fail('\\S(.*\\S)?')
  def test_rfc6991_txt__477(self):
    self.fail('(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))')
  def test_rfc6991_txt__525(self):
    self.fail('\\d*(\\.\\d*){1,127}')
  def test_rfc6991_txt__571(self):
    self.fail('\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?')
  def test_rfc7758_txt__703(self):
    self.fail('\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?')
  def test_rfc7758_txt_1358(self):
    self.fail('\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?')
  def test_rfc7895_txt__349(self):
    self.fail('\\d{4}-\\d{2}-\\d{2}')
  def test_rfc8194_txt__905(self):
    self.fail('Z|[\\+\\-]\\d{2}:\\d{2}')
  def test_rfc8040_txt_4713(self):
    self.fail('\\d{4}-\\d{2}-\\d{2}')
  def test_rfc8525_txt__550(self):
    self.fail('\\d{4}-\\d{2}-\\d{2}')
  def test_rfc8819_txt__311(self):
    self.fail('[\\S ]+')

  def succeed(self, expression):
    self.assertTrue(check(expression))
  def fail(self, expression):
    self.assertFalse(check(expression))