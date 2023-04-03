from tests import unittest
import iregexp

class SomeTests(unittest.TestCase):

    def test_sample(self):
        result = iregexp.hello_world()
        self.assertEqual('dude!', result)
