#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[PyICM]* :: SERVICE: create a non-interactive git-shell processing account. USER: issues triggers.
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Scope And Purpose                                                  :Overview:
*** +
*** Purpose: Allows for USER to trigger immediate actions on SERVICE using git-shell and git hooks.
*** Scope: This ICM covers both SERVICE and USER sides.
*** -
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]
** +
** On SERVICE, run fullServiceUpdate -- create git-repos and install git-hooks.
** On USER, run fullUserUpdate -- install keys --  clone git-repos and push.
**      [End-Of-Usage]
"""


icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Under Development -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO complete implementation of all commands.
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "cntnrGitShTriggers"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202112191841"
####+END:

####+BEGIN: bx:icm:py:status :status "Production"
icmInfo['status']  = "Production"
####+END:

icmInfo['credits'] = ""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/icmInfo-mbNedaGplByStar.py"
icmInfo['authors'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['copyright'] = "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]"
icmInfo['licenses'] = "[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"
icmInfo['maintainers'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['contacts'] = "[[http://mohsen.1.banan.byname.net/contact]]"
icmInfo['partOf'] = "[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]"
####+END:


####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=   " :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=    :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import collections
import os
# import shutil
# import invoke
# import tempfile

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
from bisos.icm import clsMethod

from bisos import bpf

import getpass
from abc import ABC, abstractmethod

####+BEGIN: bx:icm:python:icmItem :itemType "=ImportICMs=" :itemTitle "*Imported Commands Modules*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =ImportICMs= :: *Imported Commands Modules*  [[elisp:(org-cycle)][| ]]
"""
####+END:

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'blee.icmPlayer.bleep',
]

####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :comment "Params Spec for: --rosu" :funcType "FmWrk" :retType "Void" :deco "" :argsList "icmParams"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FmWrk :: /commonParamsSpecify/ =Params Spec for: --rosu= retType=Void argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    """
** --rosu (Remote Operations Service Unit. Name of the ROS)
    """
    icmParams.parDictAdd(
        parName='rosu',
        parDescription="Remote Operations Service Unit. Name of the ROS",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rosu',
    )

####+BEGIN: bx:icm:python:func :funcName "g_paramsExtraSpecify" :comment "FrameWork: ArgsSpec" :funcType "FmWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FmWrk :: /g_paramsExtraSpecify/ =FrameWork: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_paramsExtraSpecify(
    parser,
):
####+END:
    """
** Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    bleep.commonParamsSpecify(icmParams)

    clsMethod.commonParamsSpecify(icmParams)  # --cls, --method

    commonParamsSpecify(icmParams)

    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)

    return

####+BEGIN: bx:icm:python:icmItem :itemType "=Currents=  " :itemTitle "*Currents -- curBpoId, curSi*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Currents=   :: *Currents -- curBpoId, curSi*  [[elisp:(org-cycle)][| ]]
"""
####+END:


####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/curGetBxOSr.py"
def curGet_bxoId(): return bxCurrentsConfig.bxoId_fpObtain(configBaseDir=None)
def curGet_sr(): return bxCurrentsConfig.sr_fpObtain(configBaseDir=None)
def cmndParsCurBxoSr(cps): cps['bxoId'] = curGet_bxoId(); cps['sr'] = curGet_sr()
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "examples" :cmndType "Cmnd-FmWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "bpoId sivd" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cmnd-FmWrk :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt=bpoId sivd argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bpoId', 'sivd', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        sivd=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {'bpoId': bpoId, 'sivd': sivd, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            bpoId = callParamsDict['bpoId']
            sivd = callParamsDict['sivd']

####+END:
        docStr = """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all on one place.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        def cpsInit(): return collections.OrderedDict()
        cmndArgs = "" ; cps=cpsInit() ;
        def menuItem(verbosity='little', comment=""): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity, comment=comment) # 'little' or 'none'
        # def extMenuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmName=icmExName, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        #oneBpo = "pmi_ByD-100001"
        #oneBpo = curGet_bxoId()

        #if bpoId: oneBpo = bpoId
        # if si: oneSiRelPath = si

        # logControler = icm.LOG_Control()
        # logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        icm.cmndExampleMenuChapter('*BISOS System (gitSsh) Account*')
        execLineEx("""\
bisosAccounts.sh
bisosAccounts.sh -h -v -n showRun -i gitSshBxSysAcctVerify  # Info
bisosAccounts.sh -h -v -n showRun -i gitSshBxSysAcctCreate  # acctAdd, report
bisosAccounts.sh -h -v -n showRun -i userAcctsDelete gitSsh""")

        icm.cmndExampleMenuChapter('*Full Actions*')
        cmndName = "fullServiceUpdate" ; menuItem(verbosity='little')
        cmndName = "fullUserUpdate" ; menuItem(verbosity='little')

        icm.cmndExampleMenuChapter('*Home Account And Keys Setup*')
        cmndName = "gitSshAccountCreate" ; menuItem(verbosity='little')
        cmndName = "noInteractiveShellSetup" ; menuItem(verbosity='little')

        icm.cmndExampleMenuChapter('*Invoker (client) Side:: SSH Setup*')
        cmndName = "gitSsh_invoker_sshUsgSetup" ; cmndArgs = "localhost" ; menuItem()
        cmndName = "gitSsh_invoker_sshUsgSetup" ; cmndArgs = "localhost performerCntnrId" ; menuItem()
        cmndName = "gitSsh_invoker_sshUsgLogin" ; cmndArgs = "localhost" ; menuItem()

        icm.cmndExampleMenuChapter('*Performer (server) Side:: SSH Setup*')
        cmndName = "gitSsh_performer_sshSetup" ; cmndArgs = "localhost ~/.ssh/id_rsa.pub" ; menuItem(verbosity='little')

        icm.cmndExampleMenuChapter('*Performer (server) Side:: Repos Create And Triggers Setup*')
        cmndName = "gitSsh_performer_repo_jekyll" ; cmndArgs = "" ; menuItem(verbosity='little', comment="#create repo in ~gitSsh/trigger-jekyll")

        icm.cmndExampleMenuChapter('*Invoker (client) Side:: Trigger With Git Push*')
        cmndName = "gitSsh_invoker_repo_jekyll" ; cmndArgs = "/bisos/var/gitSsh/invoker" ; menuItem(verbosity='little', comment="# clone baseDir")
        cmndName = "gitSsh_invoker_trigger_jekyll" ; cmndArgs = "/bisos/var/gitSsh/invoker/trigger-jekyll" ; menuItem(verbosity='little', comment="# repo baseDir")

        return(cmndOutcome)


####+BEGIN: bx:icm:py3:section :title "ICM Actions: Full Setup"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *ICM Actions: Full Setup*  [[elisp:(org-cycle)][| ]]
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "fullServiceUpdate" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /fullServiceUpdate/ =SERVICE= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class fullServiceUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Preformed fullActions, AcctCreat, NonInteractive, ReposCreate
***** TODO Not implemeted yet.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        print("AAA")
        print(self.docStrClass())

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "fullUserUpdate" :comment "USER" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /fullUserUpdate/ =USER= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class fullUserUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Preformed fullActions, AcctCreat, NonInteractive, ReposCreate
***** TODO Not implemeted yet.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        print("AAA")
        print(self.docStrClass())

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSshAccountCreate" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSshAccountCreate/ =SERVICE= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSshAccountCreate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create the account using _bisosAccounts.sh_
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        shIcmComOpts = bpf.shIcm.comOpts(self)

        if not bpf.subProc.WOpW(invedBy=self,).bash(
                f"""bisosAccounts.sh {shIcmComOpts} -i gitSshBxSysAcctVerify""",
        ).exitCode():
            icm.LOG_here("gitSsh acct is in place -- creation skipped")
        else:
            if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""bisosAccounts.sh {shIcmComOpts} -i gitSshBxSysAcctCreate""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "noInteractiveShellSetup" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /noInteractiveShellSetup/ =SERVICE= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class noInteractiveShellSetup(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        docStr = """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create ~gitSsh/git-shell-commands if needed
***** TODO For now this is a bash translation. Needs to be done in pure python.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        gitSshCommandsBaseDir = os.path.join(
            os.path.expanduser("~gitSsh"),
            "git-shell-commands",
        )
        if os.path.isdir(gitSshCommandsBaseDir):
            icm.LOG_here(f"{gitSshCommandsBaseDir} is in place -- creation skipped")
        else:
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSsh  mkdir {gitSshCommandsBaseDir}""",
            )

        noInteractiveLoginFileContent = """\
#!/usr/bin/env bash

printf '%s\\n' "Authenticated as $USER user, but interactive logins are disabled."

exit 128
"""
        gitSshNoInteractiveLogingPath = os.path.join(
            gitSshCommandsBaseDir,
            "no-interactive-login",
        )
        bpf.pyRunAs.as_gitSsh_writeToFile(
            gitSshNoInteractiveLogingPath,
            noInteractiveLoginFileContent,
        )
        bpf.subProc.WOpW(invedBy=self,).bash(
            f"""sudo -u gitSsh chmod +x {gitSshNoInteractiveLogingPath}""",
        )
        print(
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""ls -l {gitSshNoInteractiveLogingPath}""",
            ).stdout
        )

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:py3:section :title "ICM Actions: Invoker And Performer Credentials Setup"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *ICM Actions: Invoker And Performer Credentials Setup*  [[elisp:(org-cycle)][| ]]
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSsh_invoker_sshUsgSetup" :comment "USER" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSsh_invoker_sshUsgSetup/ =USER= parsMand= parsOpt= argsMin=1 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSsh_invoker_sshUsgSetup(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create an entry in ~/.ssh/config for each performer of args.
***** Process each arg as a performer cntnrId  using usgBpoSshCustomManage.sh. Adds to ~/.ssh/config.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        curUser = getpass.getuser()

        curUserSshPrivKeyFile = os.path.join(
            os.path.expanduser("~"),
            ".ssh",
            "id_rsa",
        )

        shIcmComOpts = bpf.shIcm.comOpts(self)

        for each in effectiveArgsList:  # type: ignore
            gitSshLabel = f"gitSsh-{each}"
            if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""usgBpoSshCustomManage.sh {shIcmComOpts} -p usg={curUser} -i usgCustomFullUpdate {gitSshLabel} {curUserSshPrivKeyFile} {each}  gitSsh 22""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: process each as any cntnr -- 0&9999
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cntnrs",
            argDefault='localhost',
            argChoices='any',
            argDescription="Process Each",
        )

        return cmndArgsSpecDict

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSsh_invoker_sshUsgLogin" :comment "USER" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSsh_invoker_sshUsgLogin/ =USER= parsMand= parsOpt= argsMin=1 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSsh_invoker_sshUsgLogin(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Login to each arg which is a container/performer.
***** For each, there should be no password prompt. But login should be declined.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        for each in effectiveArgsList:  # type: ignore
            gitSshLabel = f"gitSsh-{each}"
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""ssh {gitSshLabel}""",
            )

        return icm.opSuccessAnNoResult(cmndOutcome)

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: process each as any cntnr -- 0&9999
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cntnrs",
            argDefault='localhost',
            argChoices='any',
            argDescription="Process Each",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSsh_performer_sshSetup" :comment "SERVICE" :parsMand "" :parsOpt "" :argsMin "2" :argsMax "2" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSsh_performer_sshSetup/ =SERVICE= parsMand= parsOpt= argsMin=2 argsMax=2 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSsh_performer_sshSetup(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 2, 'Max': 2,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET_
***** arg1 is cntnrName, arg2 is pubKeyFile.
***** Add pub key to authorized file. Change permissions.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        cntnrName = effectiveArgsList[0]  # type: ignore
        pubKeyFile = effectiveArgsList[1]  # type: ignore
        #

        if cntnrName != "localhost":
            print("Unimplemented")
            return icm.opSuccessAnNoResult(cmndOutcome)

        gitSshAuthorizedFile = os.path.join(
            os.path.expanduser("~gitSsh"),
            ".ssh",
            "authorized_keys",
        )

        with open(pubKeyFile, 'r') as file:
            pubKeyAsStr = file.read().rstrip()

        if not bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSsh grep "{pubKeyAsStr}" {gitSshAuthorizedFile}""",
        ).exitCode():
            icm.LOG_here(f"pubKey already in {gitSshAuthorizedFile}")
            return icm.opSuccessAnNoResult(cmndOutcome)

        if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""cat {pubKeyFile} | sudo -u gitSsh tee -a {gitSshAuthorizedFile}""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self,).bash(
            f"""sudo -u gitSsh chmod go-w {gitSshAuthorizedFile}""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))
        print(
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSsh ls -l {gitSshAuthorizedFile}""",
            ).stdout
        )

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="cntnr",
            argDefault='localhost',
            argChoices='any',
            argDescription="Container to which pubKey will be added.",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="pubKey",
            argDefault='~gitSsh/.ssh/id_rsa.pub',
            argChoices='any',
            argDescription="pubKey to be added to cntnr.",
        )
        return cmndArgsSpecDict


####+BEGIN: bx:icm:py3:section :title "ICM Actions: RosuAP Create -- Invoker And Performer"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *ICM Actions: RosuAP Create -- Invoker And Performer*  [[elisp:(org-cycle)][| ]]
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSsh_performer_rosuAp_create" :comment "SERVICE" :parsMand "rosu rosuAp" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSsh_performer_rosuAp_create/ =SERVICE= parsMand=rosu rosuAp parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSsh_performer_rosuAp_create(icm.Cmnd):
    cmndParamsMandatory = [ 'rosu', 'rosuAp', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rosu=None,         # or Cmnd-Input
        rosuAp=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {'rosu': rosu, 'rosuAp': rosuAp, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            rosu = callParamsDict['rosu']
            rosuAp = callParamsDict['rosuAp']

####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Create the repo named rosu, if it does not exist.
***** Repo Create; Create post-./post-receive
***** In complete implementation -- not this -- There is a rosuAP create service to which invoker provides rosuAP.
***** This is a short cut implementation, where rosu and rosuAP are the same and when this is implemented on performer.
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        repoName = f"{rosu}.git"

        repoBaseDir = os.path.join(
            os.path.expanduser("~gitSsh"),
            repoName,
        )
        if os.path.isdir(repoBaseDir):
            icm.LOG_here(f"{repoBaseDir} is in place -- creation skipped")
            return icm.opSuccessAnNoResult(cmndOutcome)
        else:
            if bpf.subProc.WOpW(invedBy=self,).bash(
                f"""sudo -u gitSsh mkdir {repoBaseDir}""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

            if bpf.subProc.WOpW(invedBy=self, cd=repoBaseDir).bash(
                    f"""sudo -u gitSsh git init --bare""",
            ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        #
        # NOTYET, Cleanup sammy ...
        #
        postReceiveHookContent = """\
#!/usr/bin/env bash

#
# General purpose operations dispatch
#

GIT_REPO=$HOME/sammy-blog.git
TMP_GIT_CLONE=/tmp/sammy-blog
PUBLIC_WWW=/var/www/html

dateTag=$(date +%y%m%d%H%M%S)

echo ${TMP_GIT_CLONE} > /tmp/trigger.${dateTag}

exit
"""
        postReceiveHookPath = os.path.join(
            repoBaseDir,
            "hooks",
            "post-receive",
        )
        bpf.pyRunAs.as_gitSsh_writeToFile(
            postReceiveHookPath,
            postReceiveHookContent,
        )
        bpf.subProc.WOpW(invedBy=self,).bash(
            f"""sudo -u gitSsh chmod +x {postReceiveHookPath}""",
        )
        print(
            bpf.subProc.WOpW(invedBy=self,).bash(
                f"""ls -l {postReceiveHookPath}""",
            ).stdout
        )

        return icm.opSuccessAnNoResult(cmndOutcome)



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSsh_invoker_rosuAp_create" :comment "USER" :parsMand "rosu" :parsOpt "" :argsMin "0" :argsMax "2" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSsh_invoker_rosuAp_create/ =USER= parsMand=rosu parsOpt= argsMin=0 argsMax=2 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSsh_invoker_rosuAp_create(icm.Cmnd):
    cmndParamsMandatory = [ 'rosu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 2,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rosu=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {'rosu': rosu, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            rosu = callParamsDict['rosu']

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Use arg0 and param rosu to clone
***** update file. add .; commit; push
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        cmndArg0 = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList) # type: ignore
        repoBase = cmndArg0  # type: ignore

        if not os.path.isdir(repoBase):
            return(icm.EH_badOutcome(cmndOutcome))

        repoName = rosu

        if os.path.isdir(os.path.join(repoBase, repoName)):
            icm.LOG_here(f"{os.path.join(repoBase, repoName)} is in place -- git-cloning skipped")
            return icm.opSuccessAnNoResult(cmndOutcome)

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git clone gitSsh@gitSsh-localhost:{rosu}.git""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoBase",
            argDefault='/bisos/var/gitSsh/invoker',
            argChoices='any',
            argDescription="Base dir in which repo will be cloned.",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSsh_inv_opAP_create" :comment "USER" :parsMand "rosu" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSsh_inv_opAP_create/ =USER= parsMand=rosu parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSsh_inv_opAP_create(icm.Cmnd):
    cmndParamsMandatory = [ 'rosu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rosu=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {'rosu': rosu, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            rosu = callParamsDict['rosu']

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Creates an invokation Access Point
***** update file. add .; commit; push
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        repoBase = effectiveArgsList[0]  # type: ignore

        if not os.path.isdir(repoBase):
            icm.EH_problem_usageError(f"Missing {repoBase}")
            return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""date | tee -a oneFile""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git add .""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git commit -m "Auto Generated." """,
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git push""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoBase",
            argDefault='/tmp/trigger-jekyll',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="palsId",
            argDefault='thisPalsId',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        return cmndArgsSpecDict



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "gitSsh_invoker_trigger_jekyll" :comment "USER" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /gitSsh_invoker_trigger_jekyll/ =USER= parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class gitSsh_invoker_trigger_jekyll(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:
        docStr = """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] NOTYET_
***** update file. add .; commit; push
        """
        if self.docStrClassSet(docStr,): return cmndOutcome

        repoBase = effectiveArgsList[0]  # type: ignore

        if not os.path.isdir(repoBase):
            icm.EH_problem_usageError(f"Missing {repoBase}")
            return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""date | tee -a oneFile""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git add .""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git commit -m "Auto Generated." """,
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        if bpf.subProc.WOpW(invedBy=self, cd=repoBase).bash(
                f"""git push""",
        ).isProblematic():  return(icm.EH_badOutcome(cmndOutcome))

        return icm.opSuccessAnNoResult(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification: cntnr and pubKey
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repoBase",
            argDefault='/tmp/trigger-jekyll',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="palsId",
            argDefault='thisPalsId',
            argChoices='any',
            argDescription="Base dir in which repo will be created.",
        )
        return cmndArgsSpecDict


####+BEGIN: bx:icm:py3:section :title "Supporting Classes And Functions"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:dblock:python:class :className "ROSU" :superClass "object" :comment "Remote Operations Service Unit" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /ROSU/ object =Remote Operations Service Unit=  [[elisp:(org-cycle)][| ]]
"""
class ROSU(object):
####+END:
    """
** Abstraction of Remote Operations Service Unit.
"""
####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosuName: str,
            rosd: str,
    ):
        self._rosuName = rosuName
        self._rosd = rosd

####+BEGIN: bx:icm:py3:method :methodName "rosuName" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosuName/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosuName(
####+END:
            self,
    ):
        return self._rosuName

####+BEGIN: bx:icm:py3:method :methodName "rosd" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosd/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosd(
####+END:
            self,
    ):
        """
*** ROS Description. The Contract Specification. Points to a file.
        """
        return self._rosd


####+BEGIN: bx:dblock:python:class :className "RosuAccessPoint" :superClass "object" :comment "ROSU Access Point" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /RosuAccessPoint/ object =ROSU Access Point=  [[elisp:(org-cycle)][| ]]
"""
class RosuAccessPoint(object):
####+END:
    """
** Abstraction of ROSU Access Point
"""

    rosuBase = "/bisos/var/gitSsh/performer"

####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosu: ROSU,
            rosuApName: str,
            performerAddr: str,
    ):
        self._rosu = rosu
        self._rosuApName = rosuApName
        self._performerAddr = performerAddr

####+BEGIN: bx:icm:py3:method :methodName "rosu" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosu/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosu(
####+END:
            self,
    ):
        return self._rosu

####+BEGIN: bx:icm:py3:method :methodName "rosuApName" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosuApName/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosuApName(
####+END:
            self,
    ):
        return self._rosuApName

####+BEGIN: bx:icm:py3:method :methodName "performerAddr" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /performerAddr/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def performerAddr(
####+END:
            self,
    ):
        return self._performerAddr


####+BEGIN: bx:dblock:python:class :className "GitSsh_RosuAccessPoint" :superClass "RosuAccessPoint" :comment "ROSU Access Point" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /GitSsh_RosuAccessPoint/ RosuAccessPoint =ROSU Access Point=  [[elisp:(org-cycle)][| ]]
"""
class GitSsh_RosuAccessPoint(RosuAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    rosuBase = "/bisos/var/gitSsh/performer"

####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosu: ROSU,
            rosuApName: str,
            performerAddr: str,
    ):
        self._rosu = rosu
        self._rosuApName = rosuApName
        self._performerAddr = performerAddr

####+BEGIN: bx:icm:py3:method :methodName "rosu" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosu/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosu(
####+END:
            self,
    ):
        return self._rosu

####+BEGIN: bx:icm:py3:method :methodName "rosuApName" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosuApName/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosuApName(
####+END:
            self,
    ):
        return self._rosuApName

####+BEGIN: bx:icm:py3:method :methodName "performerAddr" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /performerAddr/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def performerAddr(
####+END:
            self,
    ):
        return self._performerAddr




####+BEGIN: bx:dblock:python:class :className "OperationAccessPoint" :superClass "object" :comment "Operation Access Point" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /OperationAccessPoint/ object =Operation Access Point=  [[elisp:(org-cycle)][| ]]
"""
class OperationAccessPoint(ABC):
####+END:
    """
** Abstraction of An Op AP.
"""

####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosuAp: RosuAccessPoint,
    ):
        self._rosuAp = rosuAp

####+BEGIN: bx:icm:py3:method :methodName "rosuAp" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosuAp/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosuAp(
####+END:
            self,
    ):
        return self._rosuAp

####+BEGIN: bx:icm:py3:method :methodName "invIdCreate" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invIdCreate/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invIdCreate(
####+END:
            self,
    ):
        self._invId = "NOTYET"  # datetag, plus file check

####+BEGINNOT: bx:icm:py3:method :methodName "invId" :deco "property abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invId/ deco=property abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @property
    @abstractmethod
    def invId(
####+END:
            self,
    ):
        return self._invId

####+BEGIN: bx:icm:py3:method :methodName "invoke" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invoke/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invoke(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:icm:py3:method :methodName "invokeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        pass

####+BEGIN: bx:icm:py3:method :methodName "invokeOutcomeRetreive" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeOutcomeRetreive/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeOutcomeRetreive(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        pass


####+BEGIN: bx:icm:py3:method :methodName "perform" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /perform/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def perform(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        pass

####+BEGIN: bx:icm:py3:method :methodName "performOutcomeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /performOutcomeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def performOutcomeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        pass

####+BEGIN: bx:dblock:python:class :className "GitSsh_InvokerOpAP" :superClass "OperationAccessPoint" :comment "Operation Access Point" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /GitSsh_InvokerOpAP/ OperationAccessPoint =Operation Access Point=  [[elisp:(org-cycle)][| ]]
"""
class GitSsh_InvokerOpAP(OperationAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""


####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosuAp: RosuAP,
    ):
        self._rosuAp = rosuAp

####+BEGIN: bx:icm:py3:method :methodName "rosuAp" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosuAp/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosuAp(
####+END:
            self,
    ):
        return self._rosuAp

####+BEGIN: bx:icm:py3:method :methodName "invokeIdCreate" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeIdCreate/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeIdCreate(
####+END:
            self,
    ):
        self._id = "NOTYET"  # datetag, plus file check

####+BEGIN: bx:icm:py3:method :methodName "id" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /id/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def id(
####+END:
            self,
    ):
        return self._id

####+BEGIN: bx:icm:py3:method :methodName "invoke" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invoke/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invoke(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:icm:py3:method :methodName "invokeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:icm:py3:method :methodName "invokeOutcomeRetreive" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeOutcomeRetreive/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeOutcomeRetreive(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")


####+BEGIN: bx:icm:py3:method :methodName "perform" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /perform/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def perform(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:icm:py3:method :methodName "performOutcomeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /performOutcomeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def performOutcomeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")



####+BEGIN: bx:dblock:python:class :className "GitSsh_PerformerOpAP" :superClass "OperationAccessPoint" :comment "Operation Access Point" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /GitSsh_PerformerOpAP/ OperationAccessPoint =Operation Access Point=  [[elisp:(org-cycle)][| ]]
"""
class GitSsh_PerformerOpAP(OperationAccessPoint):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""


####+BEGIN: bx:icm:py3:method :methodName "__init__" :deco "default"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /__init__/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
####+END:
            self,
            rosuAp: RosuAP,
    ):
        self._rosuAp = rosuAp

####+BEGIN: bx:icm:py3:method :methodName "rosuAp" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /rosuAp/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def rosuAp(
####+END:
            self,
    ):
        return self._rosuAp

####+BEGIN: bx:icm:py3:method :methodName "invokeIdCreate" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeIdCreate/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeIdCreate(
####+END:
            self,
    ):
        self._id = "NOTYET"  # datetag, plus file check

####+BEGIN: bx:icm:py3:method :methodName "id" :deco "property"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /id/ deco=property  [[elisp:(org-cycle)][| ]]
"""
    @property
    def id(
####+END:
            self,
    ):
        return self._id

####+BEGIN: bx:icm:py3:method :methodName "invoke" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invoke/ deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def invoke(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:icm:py3:method :methodName "invokeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:icm:py3:method :methodName "invokeOutcomeRetreive" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /invokeOutcomeRetreive/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def invokeOutcomeRetreive(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")


####+BEGIN: bx:icm:py3:method :methodName "perform" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /perform/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def perform(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")

####+BEGIN: bx:icm:py3:method :methodName "performOutcomeSubmit" :deco "abstractmethod"
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-    :: /performOutcomeSubmit/ deco=abstractmethod  [[elisp:(org-cycle)][| ]]
"""
    @abstractmethod
    def performOutcomeSubmit(
####+END:
            self,
            opName: str,
            opParams: str,
    ):
        """
*** Look into rosd, subject opName to access control, then invoke
        """
        print(f"{opName}{opParams}")



####+BEGIN: bx:icm:py3:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:py3:main :mainType  "withExamples" :comment "Common"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Framework=  ::   __main__ g_icmMain :: /withExamples/ =Common=  [[elisp:(org-cycle)][| ]]
"""
#
# ICM Main Type is: withExamples
#
if __name__ == "__main__":
    icm.g_icmMain(
        icmInfo=icmInfo,
        noCmndEntry=examples, # noCmndEntry=mainEntry,
        extraParamsHook=g_paramsExtraSpecify,
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGINNOT: bx:icm:py3:section :title "Unused Facilities -- Temporary Junk Yard"
"""
* +
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:py3:section :title "End Of Editable Text"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    :: *End Of Editable Text*  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
