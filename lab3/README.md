# ProcessOrganization_lab3

1.Title: Computational Process Organization  Lab3

2.Group Member: jiabin Yu,kang yang

3.Group Name: helloworld

4.Date：    2020 .05.29
5.Variant description :  Command line interface builder
Features of a library:
	1.support of flags with default values (python3 --version, python3 -V, python -v);
	2.support of position arguments (python3 module.py, cat file1 file2);
	3.support named arguments with default values (python3 -m module_name);
	4.support of sub-commands with a different set of arguments (docker ps, docker exec);
	5.automatic help and error message generation;
	6.support type conversation for arguments value (e.g., head -n 5 conversation string “5” to int value 5);


6.Synopsis:We use the click library to implement our command-line builder in the form of closures.

7.Contribution Summary:Yang Kang's main contribution is in the testing part, and Yu Jiabin's main contribution is in the writing part of the builder

8.Explanation of taken design decisions and analysis:Command line interface builder is implemented with the help of Click library, which makes the implementation simple. We use the decorator in click to implement our Command line interface builder

9.Work Demonstration:The test file is saved in the corresponding test.py. All you need to do is run it in pycharm.

10.Conclusion:This time the lab is not simple. We used the click library to complete the lab that meets the requirements. First of all, we learned and learned to use the click library, and we have a new understanding of programming, such as closures, and also understand the python default The general implementation of the Command line interface builder