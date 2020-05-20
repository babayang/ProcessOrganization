# ProcessOrganization_lab2

1.Title: Computational Process Organization  Lab2

2.Group Member: jiabin Yu,kang yang

3.Group Name: helloworld

4.Date：    2020 .05.20

5.Variant description :  Regular expression  which should support the following:
	1.Support special characters: \, ^, ., $, *, +, |, ( ).
	2.Support functions: match, group.
	3.Visualization as a finite state machine (state diagram or table)..


6.Synopsis:We use the NFA way to write our regular expression state machine, first perform the lexical analysis of the expression, then use the bottom-up method for grammatical analysis, and then establish NFA, and finally used to match the string.

7.Contribution Summary:JiabinYu's main contribution is in the grammatical analysis and the establishment of NFA, Kangyang's main contribution is in the lexical analysis and testing

8.Explanation of taken design decisions and analysis:NFA is a non-deterministic finite state automaton, mainly after grammatical analysis, according to the analysis results, in turn establish NFA node pairs, and finally generate a complete state machine

9.Work Demonstration:The test file is saved in the corresponding test_..All you need to do is run it in pycharm.

10.Conclusion:First of all, this lab is indeed a bit difficult, but we also learned a lot of things, first of all the types and implementation of finite state machines, and secondly mainly lexical analysis, the main method of grammatical analysis, and also helped me review the principles of compilation.