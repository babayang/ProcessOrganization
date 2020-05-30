# -*- coding: utf-8 -*-

from platform import python_version
import click
import os
import socket
import datetime
import calendar
#support of flags with default values (python3 --version, python3 -V, python -v);
@click.command()
@click.option('--version','-v', help='python version', nargs=0)
def OnGetVersion(version):
    click.echo("yk&yjb_1.0.0")

    
#support of position arguments (python3 module.py, cat file1 file2);
@click.command
@click.option('--path','-p',prompt='document name', help='document path', type=str)
def OnDocumentRead(sPath):
    cwdpath=os.getcwd()
    path1=os.path.join(cwdpath, sPath)
    sPathResult = path1.replace('\\', '/')
    
    with open('{}'.format(sPathResult),'r') as f:
        click.echo(f.read())

@click.command()
@click.argument('f', type=click.File())
def Cat(f):
   click.echo(f.read())

#support named arguments with default values (python3 -m module_name);
@click.command()
@click.option('--module','-m',prompt='module name', help='module_name', type=str)
def get_named_arguments(module):
    
    if module == 'GetCLIversion':
        click.echo('Our version is yk&yjb_1.0.0')
    elif module == 'GetGrounpInfo':
        sMemberName = socket.getfqdn(socket.gethostname())
        sMemberaddr = socket.gethostbyname(sMemberName)
        click.echo('{0}_id:{1}'.format(sMemberName, sMemberaddr))
    elif module == 'GetCurrenttime':
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H')
        click.echo(nowtime)
    elif module == 'GetDeveloperName':
        click.echo("KangYang&JiabinYu")

#support of sub-commands with a different set of arguments (docker ps, docker exec);
@click.group(chain=True)
@click.option('--op', default=False, nargs=0)
def sub_commands(op):
    pass

@sub_commands.command(context_settings={"ignore_unknown_options": True})
@click.argument('info', nargs=-1, type=click.Path())
def info(info):
    for i in info:
        if(i == '-i'):
            click.echo('our group name is helloworld')
        elif(i == '-a'):
            click.echo('yk and yjb')
        elif(i == '-l'):
            click.echo('third lab')
        else:
            click.echo('no such option')

@sub_commands.command(context_settings={"ignore_unknown_options": True})
@click.argument('comp', nargs=-1, type=click.Path())
def comp(comp):
    for i in comp:
        if(i == '-y'):
            y=datetime.datetime.now().year
            y=int(y)
            result = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            if result:
                click.echo('this year {} is leap year'.format(y))
            else:
                click.echo('this year {} is not leap year'.format(y))
        elif(i == '-d'):
            y=datetime.datetime.now().year
            y=int(y)
            m= datetime.datetime.now().month
            m=int(m)

            click.echo('this mouth has {} days'.format(calendar.monthrange(y,m)[1]))
        else:
            click.echo('there is no such option')


#automatic help and error message generation
@click.group(chain=True)
@click.option('--con', default=False, nargs=0)
def conversation(con):
    pass
            
@conversation.command(context_settings={"ignore_unknown_options": True})
@click.argument('num1', nargs=1, type=click.Path())
@click.argument('conv', nargs=-1, type=click.Path())
@click.argument('num2', nargs=1, type=click.Path())
def conver(num1,conv,num2):
    flag=0
    for i in conv:
        if(i == '+'):
            res=int(num1)+int(num2)
            click.echo(res)
        elif(i == '-'):
            res=int(num1)-int(num2)
            click.echo(res)
        elif(i == '*'):
            res=int(num1)*int(num2)
            click.echo(res)
        elif(i == '/'):
            res=int(num1)/int(num2)
            click.echo(res)
        elif(i == 'conversation'):
            flag=2
        if(flag==2 and i == 'int'):
            num2 = int(num2)
            click.echo('{0} is {1}'.format(num2, type(num2)))
        elif(flag==2 and i == 'float'):
            num2 = float(num2)
            click.echo('{0} is {1}'.format(num2, type(num2)))

            
            