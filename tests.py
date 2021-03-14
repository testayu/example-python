import unittest

import awesome

a="<svg onload=prompt(1)"
b="\" OR 1=1;--"
c="{{7*7}}"

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
