from cpu_common import *
from cpu_ref import *
ioname="Chest Hard Drive v0"
class HardDrive:
	def __init__(self,callPear,chestPear,returnPear,pivot):
		self.callPear=callPear
		self.chestPear=chestPear
		self.returnPear=returnPear
		self.pivot=pivot
	def action(self,i):
		if i>5:
			return self.pivot.moveY(i-5)
		if i>3:
			return self.pivot.moveZ(i-3)
		return self.pivot.moveX(i)
'''
hd.drive._pro.setFalse()
hd.drive.iAdress
'''