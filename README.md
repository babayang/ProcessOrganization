# ProcessOrganization_lab1

1.Title: Computational Process Organization  Lab1

2.Group Member: jiabin Yu,kang yang

3.Date：    2020 .05.06

4.Variant description :  Hash-map (collision resolution: open addressing, for the array you can use built-in list) based set.


5.Synopsis:This Lab mainly contains two parts, the writing of Hashmap library and the correctness test of the library

6.Contribution Summary:The main contribution of JiabinYu is in the writing part of the Hashmap library, and the main contribution of KangYang is in the correctness testing part of the library

7.Explanation of taken design decisions and analysis:The library mainly contains two parts, one is a mutable object part, and the functions in it will change the source hashmap. The main operations included in this part are adding, searching, deleting, converting to an array, etc. The other part is the immutable object part, mainly including adding , Delete, merge and other operations.

8.Work Demonstration:The test file is saved in the corresponding test_..All you need to do is run it in pycharm.

9.Conclusion:First of all, in this lab, I felt many problems that need to be considered as a library developer. An excellent container library should support both types of functions of variable objects and immutable objects. Function, which really helped us to detect many problems, we also learned to use Hypothesis library to do the test