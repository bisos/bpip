#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[ICM-gipcs_manage.py]* :: Remote Git-Shell Invoke-Perform Commands Services: GIPCS at a given Remote Op Svc Multi-Unit AP (rosmuAp)
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
**** +
**** rosmuAp = Remote Operations Service Multi-Unit Access Point
**** rosmuAp maps to a git-shell-repo
**** rosmuAp has at its root: ./apAddr / ./invs  ./state ./files rosmuSpec
**** --
**** gipcs_manage.py --perfAddr=act@cntnrId --rosmuAp=name -i create # creates osmupAP repos.
**** --
**** gipcs_manage.py --rosmuApPath=path -i inv -- anyOsmuIcm --par1 -i cmnd1 arg1
**** gipcs_manage.py --rosmuApPath=path -i perf # searches in ./invs/
**** -
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""

icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current     :: For now it is an ICM. Turn it into ICM-Lib. [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "gipcs_manage"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202201041655"
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

icmInfo['panel'] = "{}-Panel.org".format(icmInfo['moduleName'])
icmInfo['groupingType'] = "IcmGroupingType-pkged"
icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"


####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/bisos/git/auth/bxRepos/bisos/bpip1/bin/gipcs_manage.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
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

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
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

####+BEGIN: bx:icm:python:icmItem :itemType "=ImportICMs=" :itemTitle "*Imported Commands Modules*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =ImportICMs= :: *Imported Commands Modules*  [[elisp:(org-cycle)][| ]]
"""
####+END:

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'blee.icmPlayer.bleep',
]

####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :comment "Params Spec for: --aipxBase --aipxRoot" :funcType "FmWrk" :retType "Void" :deco "" :argsList "icmParams"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FmWrk :: /commonParamsSpecify/ =Params Spec for: --aipxBase --aipxRoot= retType=Void argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    """
** --rosmu (Remote Operations Service Unit. Name of the ROS)
    """
    icmParams.parDictAdd(
        parName='perfAddr',
        parDescription="Performer Address",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--perfAddr',
    )
    icmParams.parDictAdd(
        parName='perfAuSel',
        parDescription="Performer Authentication Unit Selector",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--perfAuSel',
    )
    icmParams.parDictAdd(
        parName='perfAuAddr',
        parDescription="Performer Authentication Unit Address",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--perfAuAddr',
    )
    icmParams.parDictAdd(
        parName='rosmu',
        parDescription="Remote Operations Service Multi-Unit. Name of the ROS",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rosmu',
    )
    icmParams.parDictAdd(
        parName='rosmuSel',
        parDescription="rosmu SAP Selector.",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rosmuSel',
    )
    icmParams.parDictAdd(
        parName='rosmuAp',
        parDescription="Combination of perfAuAddr+rosmu+rosmuSel",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rosmuAp',
    )
    icmParams.parDictAdd(
        parName='rosmuApPath',
        parDescription="A path to rosmuAp is available as FPs",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rosmuApPath',
    )
    icmParams.parDictAdd(
        parName='invId',
        parDescription="Remote Operations Service Unit. Name of the ROS",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--invId',
    )


####+BEGIN: bx:icm:python:func :funcName "g_paramsExtraSpecify" :comment "FmWrk: ArgsSpec" :funcType "FmWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FmWrk :: /g_paramsExtraSpecify/ =FmWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
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
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Currents=   :: *Currents -- curBpoId, curSi*  [[elisp:(org-cycle)][| ]]
"""
####+END:


####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/curGetBxOSr.py"
def curGet_bxoId(): return bxCurrentsConfig.bxoId_fpObtain(configBaseDir=None)
def curGet_sr(): return bxCurrentsConfig.sr_fpObtain(configBaseDir=None)
def cmndParsCurBxoSr(cps): cps['bxoId'] = curGet_bxoId(); cps['sr'] = curGet_sr()
####+END:


####+BEGIN: icm:py3:cmnd:classHead :cmndName "examples" :cmndType "Cmnd-FmWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "cntnrId rosmu" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cmnd-FmWrk :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt=cntnrId rosmu argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'cntnrId', 'rosmu', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        cntnrId=None,         # or Cmnd-Input
        rosmu=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
####+END:
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all in one place.
        """
        cmndOutcome = self.getOpOutcome()

        def cpsInit(): return collections.OrderedDict()
        cmndArgs = "" ; cps=cpsInit() ;
        def menuItem(verbosity, **kwArgs): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity, **kwArgs)
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        if not cntnrId:
            cntnrId = "localhost"

        if not rosmu:
            rosmu = "facterIcm"

        # rosmuApPath will look like this f"/bisos/var/gipcs/perfs/cntnrId/rosmuAp"  # will be dateTag-ed
        gipcsPerfsRoot = pathlib.Path(f"/bisos/var/gipcs/perfs")
        gipcsPerfPath = gipcsPerfsRoot.joinpath(cntnrId)
        rosmuApPath = gipcsPerfPath.joinpath(rosmu)

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        svcCmndUnit = "facterIcm.py"
        svcCmndName = "factName"
        svcCmndArgs = "networking.interfaces.lo.bindings[0].address"

        invCmndArgs = f"""-- {svcCmndUnit} -i {svcCmndName} {svcCmndArgs}"""
        perfCmndArgs = ""

        icm.cmndExampleMenuChapter('*GIPCS SAP Create*')

        cmndArgs = invCmndArgs
        cmndName = "sapCreate" ; cps=cpsInit()
        cps['perfAddr'] = cntnrId ; cps['rosmu'] = rosmu
        menuItem(verbosity='little', comment="# Under development in parts")

        icm.cmndExampleMenuChapter('*GIPCS Invoke*')

        cmndArgs = invCmndArgs
        cmndName = "inv" ; cps=cpsInit() ; cps['rosmuApPath'] = rosmuApPath
        menuItem(verbosity='little', comment="# Under development in parts")

        icm.cmndExampleMenuChapter('*GIPCS Perform*')

        cmndName = "perf" ; cps=cpsInit() ; cps['rosmuApPath'] = rosmuApPath
        menuItem(verbosity='little', comment="# Under development in parts")

        icm.cmndExampleMenuChapter('*GIPCS Obtain Invoke-Outcome*')

        cmndArgs = ""

        cmndName = "invOutcome" ; cps=cpsInit() ; cps['rosmuApPath'] = rosmuApPath
        cps['invId'] = "last"
        menuItem(verbosity='little', comment="# Under development in parts")

        return(cmndOutcome)

####+BEGIN: icm:py3:cmnd:classHead :cmndName "sapCreate" :cmndType "ICM-Cmnd"  :comment "" :parsMand "perfAddr rosmu" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /sapCreate/ parsMand=perfAddr rosmu parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class sapCreate(icm.Cmnd):
    cmndParamsMandatory = [ 'perfAddr', 'rosmu', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        perfAddr=None,         # or Cmnd-Input
        rosmu=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
####+END:
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all on one place.
        """
        cmndOutcome = self.getOpOutcome()

        return(cmndOutcome)


####+BEGIN: icm:py3:cmnd:classHead :cmndName "inv" :cmndType "ICM-Cmnd"  :comment "" :parsMand "rosmuApPath" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /inv/ parsMand=rosmuApPath parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class inv(icm.Cmnd):
    cmndParamsMandatory = [ 'rosmuApPath', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rosmuApPath=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
####+END:
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] ICM examples, all on one place.
        """
        cmndOutcome = self.getOpOutcome()

        milliSecTimeTag = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]

        aipxBase = pathlib.Path(rosmuApPath).joinpath(milliSecTimeTag)
        aipxBase.mkdir(parents=True, exist_ok=True)

        invAtBase(cmndOutcome=cmndOutcome).cmnd(
             aipxBase=aipxBase,
             argsList=argsList
        )

        # Trigger a push

        return(cmndOutcome)


####+BEGIN: icm:py3:cmnd:classHead :cmndName "perf" :cmndType "ICM-Cmnd"  :comment "" :parsMand "rosmuApPath" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /perf/ =FrameWrk: ICM Examples= parsMand=aipxRoot parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class perf(icm.Cmnd):
    cmndParamsMandatory = [ 'aipxRoot', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        aipxRoot=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
####+END:
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
        - Gets called from the hook as a result of the push
        - List dirs at root.
        - Sort in reverse order
        """
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

####+BEGIN: icm:py3:cmnd:classHead :cmndName "invPerf" :cmndType "ICM-Cmnd"  :comment "" :parsMand "aipxRoot" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /invPerf/ parsMand=aipxRoot parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
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
####+END:
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Polls
        - Keeps pulling
        - Then reads in the result.
        """
        cmndOutcome = self.getOpOutcome()

        inv(cmndOutcome=cmndOutcome).cmnd(
             aipxRoot=aipxRoot,
             argsList=argsList
        )
        perf(cmndOutcome=cmndOutcome).cmnd(
             aipxRoot=aipxRoot,
        )
        return cmndOutcome

####+BEGIN: bx:dblock:python:section :title "Class Definitions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Class Definitions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

#BEGINNOT: bx:icm:py3:main :mainType  "noCmndProcessor" :comment "Common"
####+BEGINNOT: bx:icm:py3:main :mainType  "examples" :comment "Common"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Framework=  ::   __main__ g_icmMain :: /noCmndProcessor/ =Common=  [[elisp:(org-cycle)][| ]]
"""
#
# ICM Main Type is: noCmndProcessor
#
if __name__ == "__main__":
    icm.g_icmMain(
        icmInfo=icmInfo,
        noCmndEntry=examples,
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
