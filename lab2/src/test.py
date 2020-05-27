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

    def test_start(self):
        st = "aaaaa"
        pat = "^a*"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, st)

    def test_end(self):
        st = "aaaaa"
        pat = "^a*$"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, st)


    def test_part_string(self):
        st = 'hwhwhwhwhaaaaabcccccasdzxc'
        pat = '(\*?|a+)(zx|bc*)(asd|fgh)(zxc)'
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "aaaaabcccccasdzxc")

    def test_email(self):
        st = "hhhffffsujshaaabbbccc@qq.com"
        pat="a*b*c*@qq.com"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "aaabbbccc@qq.com")

    def test_filename(self):
        st="/nihao/ykaaaaa/yjbbbbbb/yessssss"
        pat="/nihao/yka+/yjb+/yes+"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, st)

    def test_phoneNumber(self):
        st="hhh155555666667"
        pat = "^15+6*7$"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "155555666667")

    def test_notMatch(self):
        st = "qwertyuiop"
        pat = "asd*"
        result = Regex(st, pat).matchAll()
        self.assertEqual(result, "")

if __name__=="__main__":
    unittest.main()