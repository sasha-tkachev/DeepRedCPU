from cpu_common import *
from cpu_ref import *
class CDU(Unit):
 	def __init__(self, fetchRegister):
		self.fetchRegister=fetchRegister
	def getUnpackedPear(self, number):
		if number<0:
			raise Exception("negative is number is invalid")

		retPoint=Point(self.fetchRegister.dest.x,self.fetchRegister.dest.y+((number+1)*2),self.fetchRegister.dest.z)
		return Pear(retPoint,self.fetchRegister.size)
	def getCmdArg(self,order,size):
		return self.getUnpackedPear(order).getSubPear(size)
	def arg(self,order,size):
		return self.getCmdArg(order,size)
#CDU-command decoding unit
Cdu=CDU(Pear("1 11 -5",8))

