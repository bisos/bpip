#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: An =ICM= for providing jekyll service instances through siJekyll module.
"""

from unisos import icm
from bisos.pals import siJekyll


if __name__ == "__main__":
    icm.g_icmMain(
        icmInfo=siJekyll.icmInfo,
        noCmndEntry=siJekyll.examples, # noCmndEntry=mainEntry,
        extraParamsHook=siJekyll.g_paramsExtraSpecify,
        importedCmndsModules=siJekyll.g_importedCmndsModules,
    )
