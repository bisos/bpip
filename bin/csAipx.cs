#!/bin/env python
# -*- coding: utf-8 -*-
""" #+begin_org\
* *[Summary]* :: A =CmndSvc= for Audit-trailed Invoke/Perform eXection (~AIPX~) over other CommandServices using this aipx.cs.
#+end_org """

####+BEGIN: b:prog:file/proclamations :copyLeft "libreHalaal"
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
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['aipx'], }
icmInfo['version'] = '202207061729'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'aipx-Panel.org'
icmInfo['groupingType'] = 'IcmGroupingType-pkged'
icmInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
A library of dblock for b:prog:file/xxx comeega-file-elements.
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


# import os
import collections

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

from bisos.currents import bxCurrentsConfig
#from bisos.icm import clsMethod

from bisos import bpf

from datetime import datetime
import pathlib

####+BEGIN: b:python:cs:framework|importCmndsModules :cmndsModules ("blee.icmPlayer.bleep")
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~g_importedCmndsModules~ (blee.icmPlayer.bleep)
#+end_org """

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'blee.icmPlayer.bleep',
]

####+END:

####+BEGIN: bx:icm:python:func :funcType "CsFrmWrk" :funcName "commonParamsSpecify" :comment "Params Spec for: --aipxBase --aipxRoot" :retType "Void" :deco "" :argsList "icmParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-CsFrmWrk [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ =Params Spec for: --aipxBase --aipxRoot= retType=Void argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    icmParams,
):
####+END:
    """ #+begin_org {
** --rosmu (Remote Operations Service Unit. Name of the ROS)
}    #+end_org """

    icmParams.parDictAdd(
        parName='aipxBase',
        parDescription="Remote Operations Service Unit. Name of the ROS",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--aipxBase',
    )
    icmParams.parDictAdd(
        parName='aipxRoot',
        parDescription="Remote Operations Service Unit. Name of the ROS",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--aipxRoot',
    )


####+BEGIN: bx:icm:python:func :funcType "CsFrmWrk" :funcName "g_paramsExtraSpecify" :comment "FmWrk: ArgsSpec"  :retType "Void" :deco "" :argsList "parser"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-CsFrmWrk [[elisp:(outline-show-subtree+toggle)][||]] /g_paramsExtraSpecify/ =FmWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
#+end_org """
def g_paramsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    commonParamsSpecify(icmParams)

    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)

    return

####+BEGIN: bx:icm:python:icmItem :itemType "=Currents=  " :itemTitle "*Currents -- curBpoId, curSi*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Currents=   [[elisp:(outline-show-subtree+toggle)][||]] *Currents -- curBpoId, curSi*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:


####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/curGetBxOSr.py"
def curGet_bxoId(): return bxCurrentsConfig.bxoId_fpObtain(configBaseDir=None)
def curGet_sr(): return bxCurrentsConfig.sr_fpObtain(configBaseDir=None)
def cmndParsCurBxoSr(cps): cps['bxoId'] = curGet_bxoId(); cps['sr'] = curGet_sr()
####+END:


####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "CmndSvc-s" :extraInfo "class someCommand(icm.Cmnd)"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *CmndSvc-s:* |]]  class someCommand(icm.Cmnd)  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: icm:py3:cmnd:classHead :cmndName "examples" :cmndType ""  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "bpoId si" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<examples>> =FrameWrk: ICM Examples= parsMand= parsOpt=bpoId si argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bpoId', 'si', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        """FrameWrk: ICM Examples"""
####+END:
        self.cmndDocStr(f""" #+begin_org \
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Conventional top level example.
        #+end_org """)

        cmndOutcome = self.getOpOutcome()

        def cpsInit(): return collections.OrderedDict()
        cmndArgs = "" ; cps=cpsInit() ;
        def menuItem(verbosity, **kwArgs): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity, **kwArgs)
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        oneBpo = "pmi_ByD-100001"
        oneSiRelPath = "jekyll/main"

        if bpoId: oneBpo = bpoId
        if si: oneSiRelPath = si

        svcCmndUnit = "scu_jekyllSiteUpdate.py"
        svcCmndName = "jekyllSiteUpdate"

        aipxBase = f"/bisos/var/aipx/{G.icmMyName()}/example"  # no dateTag
        aipxRoot = f"/bisos/var/aipx/{G.icmMyName()}"  # will be dateTag-ed

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        icm.cmndExampleMenuChapter('*No Commands Processor*')

        execLineEx(f"""\
{G.icmMyName()}
{G.icmMyName()} --aipxBase={aipxBase} -- {svcCmndUnit} --bpoId={oneBpo} --si={oneSiRelPath} -i {svcCmndName}
{G.icmMyName()} --aipxBase={aipxBase} -i invAtBase -- {svcCmndUnit} --bpoId={oneBpo} --si={oneSiRelPath} -i {svcCmndName}\
"""
        )

        invCmndArgs = f"""-- {svcCmndUnit} --bpoId={oneBpo} --si={oneSiRelPath} -i {svcCmndName}"""
        perfCmndArgs = ""

        icm.cmndExampleMenuChapter('*AIPX Invoke*')

        cmndArgs = invCmndArgs
        cmndName = "invAtBase" ; cps=cpsInit() ; cps['aipxBase'] = aipxBase
        menuItem(verbosity='little', comment="# Under development in parts")

        cmndName = "inv" ; cps=cpsInit() ; cps['aipxRoot'] = aipxRoot
        menuItem(verbosity='little', comment="# Under development in parts")

        icm.cmndExampleMenuChapter('*AIPX Perform*')

        cmndArgs = perfCmndArgs
        cmndName = "perfAtBase" ; cps=cpsInit() ; cps['aipxBase'] = aipxBase
        menuItem(verbosity='little', comment="# Under development in parts")

        cmndName = "perf" ; cps=cpsInit() ; cps['aipxRoot'] = aipxRoot
        menuItem(verbosity='little', comment="# Under development in parts")

        icm.cmndExampleMenuChapter('*AIPX Invoke-Perform*')

        cmndArgs = invCmndArgs

        # cmndName = "invPerfAtBase" ; cps=cpsInit() ; cps['aipxBase'] = aipxBase
        # menuItem(verbosity='little', comment="# Under development in parts")

        cmndName = "invPerf" ; cps=cpsInit() ; cps['aipxRoot'] = aipxRoot
        menuItem(verbosity='little', comment="# Under development in parts")

        return(cmndOutcome)

####+BEGIN: icm:py3:cmnd:classHead :cmndName "noCmndProcessor" :cmndType ""  :comment "None CS Args Processing" :parsMand "" :parsOpt "aipxBase" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<noCmndProcessor>> =None CS Args Processing= parsMand= parsOpt=aipxBase argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class noCmndProcessor(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'aipxBase', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        aipxBase=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        """None CS Args Processing"""
####+END:
        self.cmndDocStr(f""" #+begin_org \
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  With no args, run examples. otherwise, pass args to invAtBase.
        #+end_org """)

        cmndOutcome = self.getOpOutcome()

        if argsList:
            invAtBase(cmndOutcome=cmndOutcome).cmnd(
                aipxBase=aipxBase,
                argsList=argsList,
            )
        else:
            examples().cmnd()

        return(cmndOutcome)




####+BEGIN: icm:py3:cmnd:classHead :cmndName "invAtBase" :cmndType ""  :comment "Foundational invAtBase" :parsMand "aipxBase" :parsOpt "" :argsMin "1" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<invAtBase>> =Foundational invAtBase= parsMand=aipxBase parsOpt= argsMin=1 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class invAtBase(icm.Cmnd):
    cmndParamsMandatory = [ 'aipxBase', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        aipxBase=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        """Foundational invAtBase"""
####+END:
        self.cmndDocStr(f""" #+begin_org \
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Needs a better description.
        #+end_org """)

        cmndOutcome = self.getOpOutcome()

        # cmndLineArgs = G.icmRunArgsGet().cmndArgs
        cmndLineArgs = argsList

        aipxBaseIns = pathlib.Path(aipxBase) # .joinpath('ins')
        aipxBaseIns.mkdir(parents=True, exist_ok=True)

        if cmndLineArgs[0] == "--":
            cmndLineArgs.pop(0)

        withInvModel = f"{cmndLineArgs[0]} --invModel=fps --csBase={aipxBaseIns}"
        cmndLineArgs.pop(0)

        for each in cmndLineArgs:
            withInvModel = withInvModel + " " + each

        if bpf.subProc.WOpW(invedBy=self,).bash(f"{withInvModel}",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        icm.FILE_ParamWriteToPath(
            parNameFullPath=pathlib.Path(aipxBase).joinpath('invoker'),
            parValue=G.icmMyName()
        )

        # if bpf.subProc.WOpW(invedBy=self,).bash(
        #         f"ls -l {aipxBase} {aipxBaseIns}",
        # ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self,).bash(
                f"fileParamManage.py -v 30  -i fileParamDictReadDeep {aipxBase}",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return(cmndOutcome)


####+BEGIN: icm:py3:cmnd:classHead :cmndName "inv" :cmndType ""  :comment "Invoke using invAtBase" :parsMand "aipxRoot" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<inv>> =Invoke using invAtBase= parsMand=aipxRoot parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class inv(icm.Cmnd):
    cmndParamsMandatory = [ 'aipxRoot', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        aipxRoot=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        """Invoke using invAtBase"""
####+END:
        self.cmndDocStr(f""" #+begin_org \
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Invoke based on =aipxRoot= , using [[invAtBase]] recording all relevant information.
        For each invokaction use ~milliSecTimeTag~ as a uniq tag.
        #+end_org """)

        cmndOutcome = self.getOpOutcome()

        milliSecTimeTag = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]

        aipxBase = pathlib.Path(aipxRoot).joinpath(milliSecTimeTag)
        aipxBase.mkdir(parents=True, exist_ok=True)

        invAtBase(cmndOutcome=cmndOutcome).cmnd(
             aipxBase=aipxBase,
             argsList=argsList
        )

        return(cmndOutcome)


####+BEGIN: icm:py3:cmnd:classHead :cmndName "perfAtBase" :cmndType ""  :comment "Perform At Base" :parsMand "aipxBase" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<perfAtBase>> =Perform At Base= parsMand=aipxBase parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class perfAtBase(icm.Cmnd):
    cmndParamsMandatory = [ 'aipxBase', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        aipxBase=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        """Perform At Base"""
####+END:
        self.cmndDocStr(f""" #+begin_org \
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Perform at =aipxBase=. Foundation for other perform functions.
        - Go to the base and read parameters
        - Run prog there
        - Write outcome
        - timeTag start/end
        - capture execution logs
        #+end_org """)

        cmndOutcome = self.getOpOutcome()

        baseDirPath = pathlib.Path(aipxBase,)
        if not baseDirPath.is_dir():
            return(icm.EH_badOutcome(cmndOutcome))

        if (outsPath := baseDirPath.joinpath('outs')).is_dir():
            print(f"outsPath={outsPath} exists -- skipped")
            return(cmndOutcome)

        #print(f"processing outsPath={outsPath}")
        #print(f"Reading aipxBase={aipxBase}")

        results = icm.FILE_paramDictReadDeep(
            interactive=False,
            inPathList=[aipxBase,],
        )

        cmndParams = dict()

        #print(f"results={results}")

        for eachBaseDirAsKey in results:
            value = results[eachBaseDirAsKey]
            baseDir = pathlib.Path(eachBaseDirAsKey)
            parName = baseDir.name
            parParent = baseDir.parents[0].name

            #print(f"parName={parName}")

            if parName == 'cmndName':
                cmndName = value
            elif parName == 'icmName':
                icmName = value
            elif parName == 'invoker':
                invoker = value
            elif parParent == 'cmndPars':
                cmndParams.update({parName: value})
            else:
                icm.EH_problem_usageError(f"bad input: {eachBaseDirAsKey} -- {value}")

        performerCommand = f"{icmName} "
        for eachParam in cmndParams:
            performerCommand = f"""{performerCommand} --{eachParam}={cmndParams[eachParam]} """
        performerCommand = f"""{performerCommand} --csBase={outsPath} --perfModel='fps' -i {cmndName} # invoker={invoker}"""

        if bpf.subProc.WOpW(invedBy=self,).bash(f"{performerCommand}",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        print(cmndOutcome.error)
        print(cmndOutcome.results)

        # print(performerCommand)

        return(cmndOutcome)


####+BEGIN: icm:py3:cmnd:classHead :cmndName "perf" :cmndType ""  :comment "Uses perfAtBase" :parsMand "aipxRoot" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<perf>> =Uses perfAtBase= parsMand=aipxRoot parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class perf(icm.Cmnd):
    cmndParamsMandatory = [ 'aipxRoot', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        aipxRoot=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        """Uses perfAtBase"""
####+END:
        self.cmndDocStr(f""" #+begin_org \
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Perform at base with =aipxRoot=
        #+end_org """)

        cmndOutcome = self.getOpOutcome()

        # paths = sorted(pathlib.Path(aipxRoot).iterdir(), key=os.path.getmtime)
        paths = sorted(pathlib.Path(aipxRoot).iterdir(), reverse=True,)

        # print(paths)

        relevantPaths = []
        for each in paths:
            if each.name.isnumeric():
                relevantPaths.append(each)

        # print(relevantPaths)

        for each in relevantPaths:
            perfAtBase(cmndOutcome=cmndOutcome).cmnd(
                aipxBase=each,
            )

        return(cmndOutcome)

####+BEGIN: icm:py3:cmnd:classHead :cmndName "invPerf" :cmndType ""  :comment "inv + perf" :parsMand "aipxRoot" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] <<invPerf>> =inv + perf= parsMand=aipxRoot parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class invPerf(icm.Cmnd):
    cmndParamsMandatory = [ 'aipxRoot', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        aipxRoot=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        """inv + perf"""
####+END:
        self.cmndDocStr(f""" #+begin_org \
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Invoke and then perform recording all information in =aipxRoot=
        #+end_org """)
        cmndOutcome = self.getOpOutcome()

        inv(cmndOutcome=cmndOutcome).cmnd(
             aipxRoot=aipxRoot,
             argsList=argsList
        )
        perf(cmndOutcome=cmndOutcome).cmnd(
             aipxRoot=aipxRoot,
        )
        return cmndOutcome

####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "Class Definitions" :extraInfo ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *Class Definitions:* |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:python:cs:framework|main :csInfo "icmInfo" :noCmndEntry "noCmndProcessor" :extraParamsHook "g_paramsExtraSpecify" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~g_icmMain~ (icmInfo, _noCmndProcessor_, g_paramsExtraSpecify, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    icm.g_icmMain(
        icmInfo=icmInfo,
        noCmndEntry=noCmndProcessor,  # specify a Cmnd name
        extraParamsHook=g_paramsExtraSpecify,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
