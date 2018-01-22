#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""L2G2IS: MEMS motion sensor: Ultra-compact two-axis gyroscope for optical image stabilization"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	WHO_AM_I = 0
	TEMP_OUT = 1
	OUT_X = 3
	OUT_Y = 5
	STATUS_REG = 9
	CTRL_REG1 = 11
	CTRL_REG2 = 12
	CTRL_REG3 = 13
	ORIENT_CONFIG = 16
	OFF_X = 17
	OFF_Y = 18
	CTRL_REG4 = 31
