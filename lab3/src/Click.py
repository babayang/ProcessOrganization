
def CommandParser():
    vCommand = {}
    def Click(sCmd):
        def OnReg(pFun):
            vCommand[sCmd] = pFun
            return pFun
        return OnReg
    def OnRun(*args):
        sCmd = args[0]
        #            print(cmd)
        if ''==sCmd:
            print('Uknown command')
            return
        else:
            vParams = sCmd.split(' ')
            sFirstPara=vParams[0]
            args = []
            kwargs = {}
            for sParam in vParams:
                # parse params
                x = sParam.split('=', maxsplit=1)
                # is dict
                if 2==len(x) :
                    kwargs[x[0]] = x[1]
                # is tuple
                elif 1==len(x) :
                    args.append(x[0])
        del args[0]
        if sFirstPara == '--infocomp' or sFirstPara == '-op':
            if vCommand.get(sFirstPara, "Unkown Command")=="Unkown Command":
                print('Uknown command')
                return
            sFirstPara = args[0]
            args = list(args)
            del args[0]
        return (vCommand.get(sFirstPara)(*args, **kwargs))

    return Click, OnRun