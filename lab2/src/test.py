import unittest
from regular_expression import *

class  RegularExpression(unittest.TestCase):
    #test *
    def test_multiplication(self):
        st = "aaaaaa"
        pat = "a*"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)

    # test +
    def test_plus(self):
        st = "aaaaaa"
        pat = "a+"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)

    #test |
    def test_or(self):
        st = "haaaa"
        pat="\*?|ha+"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)
    #test .
    def test_point(self):
        st = "haaaa"
        pat= "ha.aa"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)


    # test ()
    def test_match(self):
        st = "aaaaabcccccasdzxc"
        pat= "(\*?|a+)(zx|bc*)(asd|fgh)(zxc)"
        result = Regex(st, pat).matchAll()
        self.assertEqual(st, result)

    def test_group(self):
        st = "aaaaabcccccasdzxc"
        pat = "(\*?|a+)(zx|bc*)(asd|fgh)(zxc)"
        result = Regex(st, pat).group(2)
        self.assertEqual("bccccc", result)

if __name__=="__main__":
    unittest.main()