#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* *[Summary]* :: A =CmndSvc= for retrieving message with offlineimap from imap server with inMail info.
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['marmeeInMailRetrieve'], }
icmInfo['version'] = '202207115044'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'marmeeInMailRetrieve-Panel.org'
icmInfo['groupingType'] = 'IcmGroupingType-pkged'
icmInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

import sys
import os

import shutil

import collections

from bisos.marmee import marmeAcctsLib

from bisos.currents import currentsConfig

from bisos.bpo import bpo
from bisos.bpo import bpoRunBases

#from bisos.icm import clsMethod

from bisos import bpf

from datetime import datetime
import pathlib



####+BEGIN: b:python:cs:framework/importCmndsModules :cmndsModules ("blee.icmPlayer.bleep" "bisos.marmee.marmeAcctsLib")
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~g_importedCmndsModules~ (blee.icmPlayer.bleep bisos.marmee.marmeAcctsLib)
#+end_org """

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'blee.icmPlayer.bleep',
    'bisos.marmee.marmeAcctsLib',
]

####+END:

####+BEGIN: bx:icm:python:func :funcType "CsFrmWrk" :funcName "g_paramsExtraSpecify" :comment "FmWrk: ArgsSpec"  :retType "Void" :deco "" :argsList "parser"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-CsFrmWrk [[elisp:(outline-show-subtree+toggle)][||]] /g_paramsExtraSpecify/ =FmWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
#+end_org """
def g_paramsExtraSpecify(
    parser,
):
####+END:
    """  #+begin_org
** Module Specific Command Line Parameters. This func is passed to G_main and can not be decorated.
#+end_org """

    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    icmParams.parDictAdd(
        parName='moduleVersion',
        parDescription='Module Version',
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )

    bleep.commonParamsSpecify(icmParams)

    marmeAcctsLib.commonParamsSpecify(icmParams)

    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)

    return

####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "CmndSvc-s" :extraInfo "class someCommand(icm.Cmnd)"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *CmndSvc-s:* |]]  class someCommand(icm.Cmnd)  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

def g_opSysExit(opOutcome):
    print(opOutcome.error)
    sys.exit()

g_outcome = bpf.op.Outcome()

####+BEGIN: b:python:cs:module/cur_paramsAssign  :curParsList ("aasMarmee_bpoId" "aasMarmee_svcInMail" "aasMarmee_svcOutMail" "aasMarmee_svcProvider" "aasMarmee_svcInstance")
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Currents   [[elisp:(outline-show-subtree+toggle)][||]] ~cur_examples~ (aasMarmee_bpoId aasMarmee_svcInMail aasMarmee_svcOutMail aasMarmee_svcProvider aasMarmee_svcInstance)
#+end_org """
_parNamesList = [ 'aasMarmee_bpoId', 'aasMarmee_svcInMail', 'aasMarmee_svcOutMail', 'aasMarmee_svcProvider', 'aasMarmee_svcInstance',]
if not (curParsDictValue := currentsConfig.curParsGetAsDictValue_wOp(_parNamesList, outcome=g_outcome).results): g_opSysExit(g_outcome)
cur_aasMarmee_bpoId = curParsDictValue['aasMarmee_bpoId']
cur_aasMarmee_svcInMail = curParsDictValue['aasMarmee_svcInMail']
cur_aasMarmee_svcOutMail = curParsDictValue['aasMarmee_svcOutMail']
cur_aasMarmee_svcProvider = curParsDictValue['aasMarmee_svcProvider']
cur_aasMarmee_svcInstance = curParsDictValue['aasMarmee_svcInstance']
def cur_examples():
    icm.ex_gExecMenuItem(execLine='bx-currents.cs')
    icm.ex_gExecMenuItem(execLine='bx-currents.cs -i usgCursParsGet')
    for each in _parNamesList:
        icm.ex_gExecMenuItem(execLine=f'bx-currents.cs -v 20 -i pkgInfoParsSet {each}={curParsDictValue[each]}')
####+END:



####+BEGIN: icm:py3:cmnd:classHead :cmndName "examples" :cmndType ""  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<examples>> =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        """FrameWrk: ICM Examples"""
####+END:
        self.cmndDocStr(f""" #+begin_org ***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Conventional top level example.
        #+end_org """)

        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)


        cmndOutcome = self.getOpOutcome()

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        controlProfile = marmeAcctsLib.enabledControlProfileObtain(curGet_bxoId(), curGet_sr())
        defaultMailDom = marmeAcctsLib.enabledInMailAcctObtain(curGet_bxoId(), curGet_sr())

####+BEGIN: bx:icm:python:cmnd:subSection :title "Dev And Testing"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Dev And Testing*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:
        #icm.cmndExampleMenuChapter('*General Dev and Testing IIFs*')

        icm.cmndExampleMenuChapter('*Config File Creation Facility IIFs*')

        cmndName = "offlineimaprcUpdate" ;  cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps);
        menuItem(verbosity='none') ; menuItem(verbosity='full')

        cmndName = "offlineimaprcStdout" ;  cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps);
        menuItem(verbosity='none') ; menuItem(verbosity='full')

        configFile = withInMailDomGetOfflineimaprcPath(
            controlProfile,
            defaultMailDom,
            curGet_bxoId(),
            curGet_sr(),
        )

        icm.ANN_write(
            """ls -l {}""".format(configFile)
        )
        icm.ANN_write(
            """cat  {} """.format(configFile)
        )

        icm.cmndExampleMenuChapter('*Operation Facility IIFs -- (offlineimapRun)*')

        cmndName = "offlineimapRun" ;  cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps);
        menuItem(verbosity='none') ; menuItem(verbosity='full')

        marmeAcctsLib.examples_controlProfileManage()

        #marmeAcctsLib.examples_marmeAcctsLibControls()
        marmeAcctsLib.examples_enabledInMailAcctConfig()

        marmeAcctsLib.examples_inMailAcctAccessPars()



        return(cmndOutcome)


####+BEGIN: bx:icm:python:func :funcName "curGet_bxoId" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /curGet_bxoId/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def curGet_bxoId():
####+END:
    return "mcm"


####+BEGIN: bx:icm:python:func :funcName "curGet_sr" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /curGet_sr/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def curGet_sr():
####+END:
    return "marme/dsnProc"


####+BEGIN: bx:icm:python:func :funcName "cmndParsCurBxoSr" :funcType "void" :retType "bool" :deco "" :argsList "cps"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-void      :: /cmndParsCurBxoSr/ retType=bool argsList=(cps)  [[elisp:(org-cycle)][| ]]
"""
def cmndParsCurBxoSr(
    cps,
):
####+END:
    cps['bxoId'] = curGet_bxoId()
    cps['sr'] = curGet_sr()


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "offlineimapRun" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /offlineimapRun/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class offlineimapRun(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']

####+END:
        """
** TODO Make inMailAcct come from args not params
        """
        offlineimaprcPath = withInMailDomGetOfflineimaprcPath(
            controlProfile,
            inMailAcct,
            bxoId,
            sr,
        )

        outcome = icm.subProc_bash("""offlineimap -c {offlineimaprcPath}"""
                                    .format(offlineimaprcPath=offlineimaprcPath)
        ).log()
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "offlineimaprcUpdate" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /offlineimaprcUpdate/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class offlineimaprcUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']

####+END:
        outcome = offlineimaprcStdout().cmnd(
            interactive=False,
            inMailAcct=inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))

        offlineimaprcStr = outcome.results

        offlineimaprcPath = withInMailDomGetOfflineimaprcPath(
            controlProfile,
            inMailAcct,
            bxoId,
            sr,
        )

        rcFileFromControl = "{controlProfileBaseDir}/inMail/{inMailAcct}/conf/_offlineimaprc".format(
            # ../control/inMail/example.com/conf/_offlineimaprc
            controlProfileBaseDir=marmeAcctsLib.controlProfileBaseDirGet(
                controlProfile,
                bxoId=bxoId,
                sr=sr,
            ),
            inMailAcct=inMailAcct,
        )

        if os.path.isfile(rcFileFromControl):
            shutil.copyfile(rcFileFromControl, offlineimaprcPath)
        else:
            with open(offlineimaprcPath, "w") as thisFile:
                thisFile.write(offlineimaprcStr + '\n')

        thisPath = marmeAcctsLib.getPathForAcctMaildir(
            controlProfile,
            inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )

        try:
            os.makedirs(thisPath)
        except OSError:
            if not os.path.isdir(thisPath):
                raise

        if interactive:
            icm.ANN_here("offlineimaprcPath={val}".format(val=offlineimaprcPath))

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=offlineimaprcStr,
        )

####+BEGIN: bx:icm:python:func :funcName "withInMailDomGetOfflineimaprcPath" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "controlProfile inMailAcct bxoId sr"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /withInMailDomGetOfflineimaprcPath/ retType=bool argsList=(controlProfile inMailAcct bxoId sr)  [[elisp:(org-cycle)][| ]]
"""
def withInMailDomGetOfflineimaprcPath(
    controlProfile,
    inMailAcct,
    bxoId,
    sr,
):
####+END:
    inMailAcctConfBase = os.path.abspath(
        "{configBaseDir}"
        .format(configBaseDir=marmeAcctsLib.getPathForInMailConfig(
            controlProfile,
            inMailAcct,
            bxoId=bxoId,
            sr=sr,
        ))
    )

    try:
        os.makedirs(inMailAcctConfBase)
    except OSError:
        if not os.path.isdir(inMailAcctConfBase):
            raise

    offlineimaprcFile = os.path.join(
        inMailAcctConfBase,
        "_offlineimaprc"
    )
    return offlineimaprcFile


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "offlineimaprcStdout" :comment "" :parsMand "" :parsOpt "bxoId sr inMailAcct mboxesList ssl" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /offlineimaprcStdout/ parsMand= parsOpt=bxoId sr inMailAcct mboxesList ssl argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class offlineimaprcStdout(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'inMailAcct', 'mboxesList', 'ssl', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        mboxesList=None,         # or Cmnd-Input
        ssl=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'inMailAcct': inMailAcct, 'mboxesList': mboxesList, 'ssl': ssl, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        inMailAcct = callParamsDict['inMailAcct']
        mboxesList = callParamsDict['mboxesList']
        ssl = callParamsDict['ssl']

####+END:

        outcome = marmeAcctsLib.inMailAcctParsGet().cmnd(
            interactive=False,
            bxoId=bxoId,
            sr=sr,
            inMailAcct=inMailAcct,
            argsList=['access'],
        )
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))

        fileParamDict = outcome.results

        outcome = marmeAcctsLib.inMailAcctParsGet().cmnd(
            interactive=False,
            bxoId=bxoId,
            sr=sr,
            inMailAcct=inMailAcct,
            argsList=['retrieval']
        )
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))
        fileParamRetrievalDict = outcome.results

        mailDirFullPath = fileParamRetrievalDict['inMailAcctMboxesPath'].parValueGet()
        if not mailDirFullPath: return icm.EH_badOutcome(outcome)

        try:
            os.makedirs(mailDirFullPath)
        except OSError:
            if not os.path.isdir(mailDirFullPath):
                raise

        mboxesList = fileParamRetrievalDict['mboxesList'].parValueGet()

        foldersListStr = ""
        if mboxesList == "all":
            folderFilterLineStr = "#"
        else:
            for each in mboxesList.split():
                foldersListStr += "'INBOX.{}',".format(each)

            folderFilterLineStr = """folderfilter = lambda name: name in [ {foldersListStr} ]""".format(
                foldersListStr=foldersListStr)

        resStr = offlineimaprcTemplate().format(
            inMailAcctMboxesPath=mailDirFullPath,
            imapServer=fileParamDict['imapServer'].parValueGet(),
            userName=fileParamDict['userName'].parValueGet(),
            userPasswd=fileParamDict['userPasswd'].parValueGet(),
            ssl=fileParamRetrievalDict['ssl'].parValueGet(),
            foldersListStr=foldersListStr,
            folderFilterLine=folderFilterLineStr,
        )

        if interactive:
            print(resStr)

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=resStr
        )

####+BEGIN: bx:icm:python:func :funcName "offlineimaprcTemplate" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /offlineimaprcTemplate/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def offlineimaprcTemplate():
####+END:
    templateStr = """
[general]
accounts = MyAccount
#pythonfile = .offlineimap.py

[Account MyAccount]
localrepository = LocalIMAP
remoterepository = RemoteIMAP
# autorefresh = 5
# postsynchook = notmuch new

[Repository LocalIMAP]
type = Maildir
localfolders = {inMailAcctMboxesPath}

[Repository RemoteIMAP]
type = IMAP
sslcacertfile = /etc/ssl/certs/ca-certificates.crt
remotehost = {imapServer}
remoteuser = {userName}
remotepass = {userPasswd}
ssl = {ssl}
nametrans = lambda name: re.sub('^INBOX.', '', name)
{folderFilterLine}
# folderfilter = lambda name: name in [ {foldersListStr} ]
# folderfilter = lambda name: not (name in [ 'INBOX.spam', 'INBOX.commits' ])
# holdconnectionopen = yes
# maxconnections = 3
# foldersort = lld_cmp

"""
    return templateStr




####+BEGIN: b:python:cs:framework/main :csInfo "icmInfo" :noCmndEntry "examples" :extraParamsHook "g_paramsExtraSpecify" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~g_icmMain~ (icmInfo, _examples_, g_paramsExtraSpecify, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    icm.g_icmMain(
        icmInfo=icmInfo,
        noCmndEntry=examples,  # specify a Cmnd name
        extraParamsHook=g_paramsExtraSpecify,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGIN: b:prog:file/endOfFile :extraParams nil
""" #+begin_org
* *[[elisp:(org-cycle)][| END-OF-FILE |]]* :: emacs and org variables and control parameters
#+end_org """
### local variables:
### no-byte-compile: t
### end:
####+END:
