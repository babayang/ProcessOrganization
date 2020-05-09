import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable_version import *

class TestMutableList(unittest.TestCase):

    def test_size(self):
        self.assertEqual(size(MyHashMap(vItem=[])), 0)
        self.assertEqual(size(MyHashMap(vItem=[3, 8])), 2)
        self.assertEqual(size(MyHashMap(vItem=[6, 3, 4])), 3)

    def test_extend(self):
        self.assertEqual(extend(MyHashMap(vItem=[]),2).to_list().sort(),[2].sort())
        self.assertEqual(extend(MyHashMap(vItem=[3,67,1]), 2).to_list().sort(), [3,67,1,2].sort())
        self.assertEqual(extend(MyHashMap(vItem=[2,3]), 66).to_list().sort(), [2,3,66].sort())

    def test_remove(self):
        self.assertEqual(remove(MyHashMap(vItem=[2]),2).to_list().sort(),[].sort())
        self.assertEqual(remove(MyHashMap(vItem=[3,6,8]), 2).to_list().sort(), [3,6,8].sort())
        self.assertEqual(remove(MyHashMap(vItem=[24,5,2]), 5).to_list().sort(), [24,2].sort())

    def test_to_list(self):
        self.assertEqual(to_list(MyHashMap(vItem=[3,6,8])).sort(),[3,6,8].sort())
        self.assertEqual(to_list(MyHashMap(vItem=[17,8])).sort(), [17,8].sort())

    def test_mconcat(self):
        self.assertEqual(mconcat(MyHashMap(vItem=[22,1,2]),MyHashMap(vItem=[22,5,6])).to_list().sort(),[22,1,2,5,6].sort())
        self.assertEqual(mconcat(MyHashMap(vItem=[]),MyHashMap(vItem=[22,5,6])).to_list().sort(), [22, 5, 6].sort())

    def test_mempty(self):
        self.assertEqual(mempty(),None)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = MyHashMap()
        lst.from_list(a)
        self.assertEqual(to_list(lst).sort(),a.sort())

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = MyHashMap()
        a.from_list(lst)
        self.assertEqual(mconcat(mempty(),a), a)
        self.assertEqual(mconcat(a,mempty()), a)

    # def test_iter(self):
    #     x=[1,2,3]
    #     lst = MyHashMap()
    #     lst.from_list(x)
    #     tmp=[]
    #     try:
    #         get_next = iterator(lst)
    #         while True:
    #             tmp.append(get_next)
    #     except StopIteration:
    #         pass
        # self.assertEqual(x.sort(),tmp.sort())
        # self.assertEqual(to_list(lst).sort(),tmp)

if __name__=='__main__':
    unittest.main()