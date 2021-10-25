#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: An =ICM= for providing plone3 service instances through siPlone3 module.
"""

from unisos import icm
from bisos.pals import siPlone3


if __name__ == "__main__":
    icm.g_icmMain(
        icmInfo=siPlone3.icmInfo,
        noCmndEntry=siPlone3.examples, # noCmndEntry=mainEntry,
        extraParamsHook=siPlone3.g_paramsExtraSpecify,
        importedCmndsModules=siPlone3.g_importedCmndsModules,
    )
