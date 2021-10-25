#!/bin/env python
# -*- coding: utf-8 -*-
"""\
Summary:: An =ICM=: a small example in traditional python style -- Not COMEEGA.
"""

from unisos import icm
import collections

G = icm.IcmGlobalContext()

def g_paramsExtraSpecify(
    parser,
):
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    # G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    icmParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )
    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)
    
    return


class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)
        
        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())
        
        icm.G_commonBriefExamples()

        icm.cmndExampleMenuChapter('*argsProc*')

        cmndName = "argsProc" ; cmndArgs = "list argOne twoArg arg3" ;
        cps = collections.OrderedDict() ;
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')

        return(cmndOutcome)

class argsProc(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpec = self.cmndArgsSpec()
        if not icm.cmndArgsValidate(effectiveArgsList, cmndArgsSpec, outcome=cmndOutcome):
            return cmndOutcome

        action = effectiveArgsList[0]
        effectiveArgsList.pop(0)

        print(action)
        
        for each in effectiveArgsList:
            print(each)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

icm.g_icmMain(
    noCmndEntry=examples,
    extraParamsHook=g_paramsExtraSpecify,
)
