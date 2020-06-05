# -*- coding: utf-8 -*-

import unittest
from CLI import *


class TestLab3(unittest.TestCase):
    #test support of flags with default values
    def test_default_values(self):
        VersionResult = OnRun('--version')
        self.assertEqual(VersionResult, "yk&yjb_1.0.0")
        VersionResult = OnRun('-v')
        self.assertEqual(VersionResult, "yk&yjb_1.0.0")

    #test support of position arguments
    def test_position_arguments(self):
        result =OnRun ('-p test.txt')
        self.assertEqual(result, 'hello,world!')

    #test named arguments with default values
    def test_named_arguments(self):
        result = OnRun('-m GetCLIversion')
        self.assertEqual(result, 'Our version is yk&yjb_1.0.0')
        
        result =OnRun('-m GetGrounpInfo')
        myname = socket.getfqdn(socket.gethostname())
        myaddr = socket.gethostbyname(myname)
        self.assertEqual(result, '{0}_id:{1}'.format(myname,myaddr))
        
        result = OnRun('-m GetCurrenttime')
        nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H')
        self.assertEqual(result , '{}'.format(nowtime))

        result = OnRun('-m GetDeveloperName')
        self.assertEqual(result, 'KangYang&JiabinYu')

    #test support of sub-commands with a different set of arguments
    def test_sub_commands(self):

        result = OnRun('-op info -i')
        self.assertEqual(result, 'our group name is helloworld\n')

        result = OnRun('-op info -i -a')
        self.assertEqual(result, 'our group name is helloworld\nyk and yjb\n')
        
        result = OnRun('-op info -i -a -l')
        self.assertEqual(result, 'our group name is helloworld\nyk and yjb\nthird lab\n')

        result = OnRun('-op comp -d')

        y = datetime.datetime.now().year
        y = int(y)
        m = datetime.datetime.now().month
        m = int(m)
        self.assertEqual(result, 'this mouth has {} days'.format(calendar.monthrange(y, m)[1]))


        result =OnRun('-op comp -y')
        y=datetime.datetime.now().year
        y=int(y)
        res = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        if res:
            self.assertEqual(result, 'this year {} is leap year'.format(y))
        else:
            self.assertEqual(result, 'this year {} is not leap year'.format(y))




    #test support type conversation for arguments value
    def test_conversation(self):
        result = OnRun('--con 8 + 2')
        self.assertEqual( result, 10)
        
        result = OnRun('--con 8 - 2')
        self.assertEqual(result , 6)

        result = OnRun('--con 8 * 2')
        self.assertEqual(result, 16)
        
        result = OnRun('--con 8 / 2')
        self.assertEqual(result, 4.0)

        result = OnRun('--con 5 conversation string to int 5')

        self.assertEqual(result, '{0} is {1}'.format(5,type(int(5))))
        result = OnRun('--con 5 conversation string to float 5')
        self.assertEqual(result, '{0} is {1}'.format(5.0,type(float(5))))
        

if __name__=='__main__':
    unittest.main()