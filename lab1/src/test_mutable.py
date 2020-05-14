import unittest
from hypothesis import given
import hypothesis.strategies as st

from mutable_version import *

from mutable_version import MyHashMap


class TestMutableList(unittest.TestCase):

    def test_size(self):
        self.assertEqual(MyHashMap(vItem=[]).size(),0)
        self.assertEqual(MyHashMap(vItem=[3,8]).size(), 2)
        self.assertEqual(MyHashMap(vItem=[6,3,4]).size(), 3)

    def test_to_list(self):
        self.assertEqual(MyHashMap(vItem=[]).to_list(),[])
        self.assertEqual(MyHashMap(vItem=[6]).to_list(), [6])
        self.assertEqual(MyHashMap(vItem=[5,77]).to_list(), [5,77])

    def test_from_list(self):
        test_data =[
            [],
            ['a'],
            ['a','b']
        ]
        for e in test_data:
            lst = MyHashMap(vItem=[])
            lst.from_list(e)
            self.assertEqual(lst.to_list().sort(),e.sort())

    def test_insert(self):
        lst = MyHashMap(vItem=[])
        lst.insert(2)
        self.assertEqual(lst.to_list().sort(), [2].sort())
        lst.insert(55)
        self.assertEqual(lst.to_list().sort(),[2,55].sort())

    def test_remove(self):
        lst = MyHashMap(vItem=[2,4,7])
        lst.remove(2)
        self.assertEqual(lst.to_list().sort(),[4,7].sort())
        lst = MyHashMap(vItem=[55, 16, 7])
        lst.remove(2)
        self.assertEqual(lst.to_list().sort(), [55, 16, 7].sort())


    def test_find(self):
        lst = MyHashMap(vItem=[2,4,7])
        result =lst.find(4)
        self.assertEqual(result,True)
        result = lst.find(5)
        self.assertEqual(result, False)
        result = lst.find(7)
        self.assertEqual(result, True)

    def test_filter(self):
        lst = MyHashMap(vItem=[1,2,3,4,5,6,7,8,9])
        lst.filter(lambda x:x%2==0)
        self.assertEqual(lst.to_list().sort(),[2,4,6,8].sort())
        lst = MyHashMap(vItem=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        lst.filter(lambda x: x % 2 != 0)
        self.assertEqual(lst.to_list().sort(), [1,3,5,7,9].sort())

    def test_map(self):
        lst = MyHashMap(vItem=[])
        lst.map(str)
        self.assertEqual(lst.to_list(),[])
        lst = MyHashMap(vItem=[1,2,3,4,5])
        lst.map(str)
        self.assertEqual(lst.to_list().sort(),['1','2','3','4','5'].sort())
        lst = MyHashMap(vItem=[1, 2, 3, 4, 5])
        lst.map(lambda x:x**2)
        self.assertEqual(lst.to_list().sort(), [1,4,9,16,25].sort())


    def test_reduce(self):
        lst = MyHashMap(vItem=[1,2,3,4])
        self.assertEqual(lst.reduce(lambda a,b:a+b, 0),10)
        test_data=[
            [],
            ['a'],
            ['a','b']
        ]
        for e in test_data:
            lst = MyHashMap()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda x,_:x+1,0),lst.size())

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        lst = MyHashMap()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(b.sort(),list(set(a)).sort())

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self,a):
        lst = MyHashMap(length=len(a)+10, vItem=a)
        # lst.from_list(a)
        # print(a,lst.to_list())
        self.assertEqual(lst.size(),len(a))


    def test_iter(self):
        x =[1,2,3]
        lst = MyHashMap()
        tmp=[]
        for e in lst:
            tmp.append(e)
        self.assertEqual(x.sort(),tmp.sort())

    def test_hashCollision(self):
        lst = MyHashMap(vItem=[100,200,300])#100,200,300 have the same hash value, so the order does not change after the conflict is resolved
        self.assertEqual(lst.to_list(),[100,200,300])
        lst = MyHashMap(vItem=[16,32,48])
        self.assertEqual(lst.to_list(),[16,32,48])

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = MyHashMap()
        a.from_list(lst)
        self.assertEqual(a.mconcat(a.mempty(),a), a)
        self.assertEqual(a.mconcat(a,a.mempty()), a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        l1 = MyHashMap(vItem=a)
        l2 = MyHashMap(vItem=b)
        l3 = MyHashMap(vItem=c)
        aa = l1.mconcat(l1.mconcat(l1, l2), l3).to_list()
        bb = l1.mconcat(l1, l1.mconcat(l2, l3)).to_list()
        self.assertEqual(aa.sort(),bb.sort())



if __name__=='__main__':
    unittest.main()
