#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: An =ICM= for providing apache2 service instances through siApache2 module.
"""

from unisos import icm
from bisos.pals import siApache2


if __name__ == "__main__":
    icm.g_icmMain(
        icmInfo=siApache2.icmInfo,
        noCmndEntry=siApache2.examples, # noCmndEntry=mainEntry,
        extraParamsHook=siApache2.g_paramsExtraSpecify,
        importedCmndsModules=siApache2.g_importedCmndsModules,
    )
