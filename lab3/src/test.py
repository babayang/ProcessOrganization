# -*- coding: utf-8 -*-

import unittest
from click.testing import CliRunner
from CLI import *

class TestLab3(unittest.TestCase):
    #test support of flags with default values
    def test_default_values(self):
        runner = CliRunner()
        VersionResult = runner.invoke(OnGetVersion, ['--version'])
        self.assertEqual(VersionResult.output, "yk&yjb_1.0.0\n")
        VersionResult = runner.invoke(OnGetVersion, ['-v'])
        self.assertEqual(VersionResult.output, "yk&yjb_1.0.0\n")

    #test support of position arguments
    def test_position_arguments(self):
        runner = CliRunner()
        result = runner.invoke(Cat, ['test.txt'])
        self.assertEqual(result.output, 'hello,world!\n')

    #test named arguments with default values
    def test_named_arguments(self):
        runner = CliRunner()
        result = runner.invoke(get_named_arguments, ['-m','GetCLIversion'])
        self.assertEqual(result.output, 'Our version is yk&yjb_1.0.0\n')
        
        result = runner.invoke(get_named_arguments, ['-m','GetGrounpInfo'])
        myname = socket.getfqdn(socket.gethostname())
        myaddr = socket.gethostbyname(myname)
        self.assertEqual(result.output, '{0}_id:{1}\n'.format(myname,myaddr))
        
        result = runner.invoke(get_named_arguments, ['-m','GetCurrenttime'])
        nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H')
        self.assertEqual(result.output , '{}\n'.format(nowtime))

        result = runner.invoke(get_named_arguments, ['-m','GetDeveloperName'])
        self.assertEqual(result.output, 'KangYang&JiabinYu\n')

    #test support of sub-commands with a different set of arguments
    def test_sub_commands(self):
        runner = CliRunner()



        result = runner.invoke(sub_commands, ['--op','info','-i'])
        self.assertEqual(result.output, 'our group name is helloworld\n')

        result = runner.invoke(sub_commands, ['--op','info','-i','-a'])
        self.assertEqual(result.output, 'our group name is helloworld\nyk and yjb\n')
        
        result = runner.invoke(sub_commands, ['--op','info','-i','-a','-l'])
        self.assertEqual(result.output, 'our group name is helloworld\nyk and yjb\nthird lab\n')

        result = runner.invoke(sub_commands, ['--op','comp','-d'])

        y = datetime.datetime.now().year
        y = int(y)
        m = datetime.datetime.now().month
        m = int(m)
        self.assertEqual(result.output, 'this mouth has {} days\n'.format(calendar.monthrange(y, m)[1]))


        result = runner.invoke(sub_commands, ['--op','comp','-y'])
        y=datetime.datetime.now().year
        y=int(y)
        res = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        if res:
            self.assertEqual(result.output, 'this year {} is leap year\n'.format(y))
        else:
            self.assertEqual(result.output, 'this year {} is not leap year\n'.format(y))




    #test support type conversation for arguments value
    def test_conversation(self):
        runner = CliRunner()
        result = runner.invoke(conversation, ['--con','conver','8','+','2'])
        self.assertEqual( result.output, '{}\n'.format(10))
        
        result = runner.invoke(conversation, ['--con','conver','8','-','2'])
        self.assertEqual(result.output , '{}\n'.format(6))

        result = runner.invoke(conversation, ['--con','conver','8','*','2'])
        self.assertEqual(result.output, '{}\n'.format(16))
        
        result = runner.invoke(conversation, ['--con','conver','6','/','2'])
        self.assertEqual(result.output, '{}\n'.format(3.0))

        result = runner.invoke(conversation, ['--con','conver','5','conversation','string','to','int','5'])

        self.assertEqual(result.output, '{0} is {1}\n'.format(5,type(int(5))))
        
        result = runner.invoke(conversation, ['--con','conver','5','conversation','string','to','float','5'])
        self.assertEqual(result.output, '{0} is {1}\n'.format(5.0,type(float(5))))
        

if __name__=='__main__':
    unittest.main()