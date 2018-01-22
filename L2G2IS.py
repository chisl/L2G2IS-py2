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

from L2G2IS_constants import *

# name:        L2G2IS
# description: MEMS motion sensor: Ultra-compact two-axis gyroscope for optical image stabilization
# manuf:       STMicroelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/l2g2is.pdf
# date:        2018-01-22


# Derive from this class and implement read and write
class L2G2IS_Base:
	"""MEMS motion sensor: Ultra-compact two-axis gyroscope for optical image stabilization"""
	# Register WHO_AM_I
	# 7.1 
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register TEMP_OUT
	# 7.2 
	
	def setTEMP_OUT(self, val):
		"""Set register TEMP_OUT"""
		self.write(REG.TEMP_OUT, val, 16)
	
	def getTEMP_OUT(self):
		"""Get register TEMP_OUT"""
		return self.read(REG.TEMP_OUT, 16)
	
	# Bits TEMP_OUT
	# Temperature data.
	#           Refer to: Section 2.4: Temperature sensor on how to read the temperature
	#           sensor output data. 
	
	# Bits unused_0
	# Register OUT_X
	# 7.3 X-axis angular rate data. The value is expressed as two’s complement. 
	
	def setOUT_X(self, val):
		"""Set register OUT_X"""
		self.write(REG.OUT_X, val, 16)
	
	def getOUT_X(self):
		"""Get register OUT_X"""
		return self.read(REG.OUT_X, 16)
	
	# Bits OUT_X
	# Register OUT_Y
	# 7.4 Y-axis angular rate data. The value is expressed as two’s complement. 
	
	def setOUT_Y(self, val):
		"""Set register OUT_Y"""
		self.write(REG.OUT_Y, val, 16)
	
	def getOUT_Y(self):
		"""Get register OUT_Y"""
		return self.read(REG.OUT_Y, 16)
	
	# Bits OUT_Y
	# Register STATUS_REG
	
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits XYOR
	# X-, Y-axis data overrun. 
	# Bits XOR
	# X-axis data overrun.  
	# Bits YOR
	# Y-axis data overrun. 
	# Bits unused_0
	# Bits XYDA
	# X-, Y-axis new data available. 
	# Bits XDA
	# X-axis new data available. 
	# Bits YDA
	# Y-axis new data available. 
	# Bits unused_1
	# Register CTRL_REG1
	# 7.6 
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits BOOT
	# Reboot memory content. 
	#           Boot request is executed as soon as internal oscillator is turned-on. It is possible to set this bit while in
	#           power-down mode, in this case it will be served at the next normal mode or sleep mode. 
	
	# Bits P_DRDY
	# DRDY signal pulsed. 
	# Bits BLE
	# Big/Little Endian Data Selection. 
	# Bits SIM
	# SPI Serial Interface Mode configuration. 
	# Bits ODU
	# Output Data Update. 
	# Bits unused_0
	# Bits PW
	# Operating mode selection. 
	#           Refer to Table 19: Operating mode selection 
	
	# Register CTRL_REG2
	# 7.7 
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits LPF_O
	# Low-pass filter order selection. 
	#           Refer to Figure 9: LPF chain block diagram and Table 24: Low-pass filter cutoff frequency selection
	
	# Bits reserved_0
	# These bits must be set to ‘0’ for proper operation of the device. 
	# Bits HP_RST
	# High-pass filter reset. 
	# Bits SW_RST
	# Software reset. 
	# Bits HPF
	# High-pass filter enable. 
	# Register CTRL_REG3
	# 7.8  
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits reserved_0
	# This bits must be set to ‘0’ for proper operation of the device. 
	# Bits ST
	# Self-test enable. 
	# Bits reserved_1
	# This bits must be set to ‘0’ for proper operation of the device. 
	# Bits PP_OD
	# DRDY pin configuration. 
	# Bits reserved_2
	# These bits must be set to ‘0’ for proper operation of the device. 
	# Bits DRDY_EN
	# Data ready enable on DRDY pin. 
	#           . Section 2.3: Data-ready interrupt and synchronous reading. 
	
	# Bits LPF_D
	# Digital low-pass filter enable. 
	#           Refer to Figure 9: LPF chain block diagram and Table 24: Low-pass filter cutoff
	#           frequency selection. 
	
	# Register ORIENT_CONFIG
	# 7.9 
	
	def setORIENT_CONFIG(self, val):
		"""Set register ORIENT_CONFIG"""
		self.write(REG.ORIENT_CONFIG, val, 8)
	
	def getORIENT_CONFIG(self):
		"""Get register ORIENT_CONFIG"""
		return self.read(REG.ORIENT_CONFIG, 8)
	
	# Bits reserved_0
	# These bits must be set to ‘0’ for proper operation of the device. 
	# Bits SIGN_X
	# X-axis angular rate sign. 
	# Bits SIGN_Y
	# Y-axis angular rate sign. 
	# Bits reserved_1
	# These bits must be set to ‘0’ for proper operation of the device. 
	# Bits ORIENT
	# Directional orientation selection. 
	# Register OFF_X
	# 7.10 
	#        User offset correction register for X-axis.
	#        The value is expressed as two’s complement. 
	
	
	def setOFF_X(self, val):
		"""Set register OFF_X"""
		self.write(REG.OFF_X, val, 8)
	
	def getOFF_X(self):
		"""Get register OFF_X"""
		return self.read(REG.OFF_X, 8)
	
	# Bits OFF_X
	# Register OFF_Y
	# 7.10 
	#        User offset correction register for Y-axis.
	#        The value is expressed as two’s complement. 
	
	
	def setOFF_Y(self, val):
		"""Set register OFF_Y"""
		self.write(REG.OFF_Y, val, 8)
	
	def getOFF_Y(self):
		"""Get register OFF_Y"""
		return self.read(REG.OFF_Y, 8)
	
	# Bits OFF_Y
	# Register CTRL_REG4
	# 7.12 
	
	def setCTRL_REG4(self, val):
		"""Set register CTRL_REG4"""
		self.write(REG.CTRL_REG4, val, 8)
	
	def getCTRL_REG4(self):
		"""Get register CTRL_REG4"""
		return self.read(REG.CTRL_REG4, 8)
	
	# Bits unused_0
	# These bits must be set to ‘0’ for proper operation of the device 
	# Bits FS
	# Full-scale selection. 
	# Bits unused_1
	# These bits must be set to ‘0’ for proper operation of the device 
	# Bits HPF_BW
	# Digital high-pass filter cutoff frequency selection. 
	#           Refer to Table 33: High-pass filter cutoff frequency selection 
	
