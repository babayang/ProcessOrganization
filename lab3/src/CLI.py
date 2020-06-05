# -*- coding: utf-8 -*-

from platform import python_version
import os
import socket
import datetime
import calendar
import  Click

Click, OnRun=Click.CommandParser()


#support of flags with default values (python3 --version, python3 -V, python -v);
@Click('--version')
@Click('-v')
def OnGetVersion():
    return ("yk&yjb_1.0.0")

    
#support of position arguments (python3 module.py, cat file1 file2);
@Click('--path')
@Click('-p')
def OnDocumentRead(sPath):
    cwdpath=os.getcwd()
    path1=os.path.join(cwdpath, sPath)
    sPathResult = path1.replace('\\', '/')
    
    with open('{}'.format(sPathResult),'r') as f:
        return (f.read())


@Click('f')
def Cat(f):
   return (f.read())

#support named arguments with default values (python3 -m module_name);
@Click('--module')
@Click('-m')
def get_named_arguments(module):
    if module == 'GetCLIversion':
        return ('Our version is yk&yjb_1.0.0')
    elif module == 'GetGrounpInfo':
        sMemberName = socket.getfqdn(socket.gethostname())
        sMemberaddr = socket.gethostbyname(sMemberName)
        return ('{0}_id:{1}'.format(sMemberName, sMemberaddr))
    elif module == 'GetCurrenttime':
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H')
        return (nowtime)
    elif module == 'GetDeveloperName':
        return ("KangYang&JiabinYu")

#support of sub-commands with a different set of arguments (docker ps, docker exec);
@Click('--infocomp')
@Click('-op')
def info_comp(*op):
    pass

@Click('info')
def info(*info):
    info=list(info)
    sResult = ""
    for i in info:
        if(i == '-i'):
            sResult+='our group name is helloworld\n'
        elif(i == '-a'):
            sResult+= ('yk and yjb\n')
        elif(i == '-l'):
            sResult+=('third lab\n')
        else:
            sResult+=('no such option\n')
    return sResult

@Click('comp')
def comp(*comp):
    for i in comp:
        if(i == '-y'):
            y=datetime.datetime.now().year
            y=int(y)
            result = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            if result:
                return ('this year {} is leap year'.format(y))
            else:
                return('this year {} is not leap year'.format(y))
        elif(i == '-d'):
            y=datetime.datetime.now().year
            y=int(y)
            m= datetime.datetime.now().month
            m=int(m)

            return('this mouth has {} days'.format(calendar.monthrange(y,m)[1]))
        else:
            return('there is no such option')



            
@Click('--con')
@Click('-c')
def conver(*conv):
    conv = list(conv)
    num1 = conv[0]
    num2 = conv[-1]
    del conv[0]
    del conv[-1]
    flag=0
    for i in conv:
        if(i == '+'):
            res=int(num1)+int(num2)
            return(res)
        elif(i == '-'):
            res=int(num1)-int(num2)
            return(res)
        elif(i == '*'):
            res=int(num1)*int(num2)
            return(res)
        elif(i == '/'):
            res=int(num1)/int(num2)
            return(res)
        elif(i == 'conversation'):
            flag=2
        if(flag==2 and i == 'int'):
            num2 = int(num2)
            return('{0} is {1}'.format(num2, type(num2)))
        elif(flag==2 and i == 'float'):
            num2 = float(num2)
            return('{0} is {1}'.format(num2, type(num2)))

            
            