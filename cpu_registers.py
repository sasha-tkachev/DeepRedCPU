
from cpu_ref import pRefrence
from cpu_common import pPool, Point, Pear


class _FlagRegister():
	def __init__(self,pear):
		if not isinstance(pear,Pear):
			raise Exception("must be pear")
		self.holder=pear	
		self.carry=self.holder.bit(0)
		self.pairity=self.holder.bit(1)
		self.zero=self.holder.bit(2)
		self.sign=self.holder.bit(3)
		self.overflow=self.holder.bit(4)
	def alureset():
		return "/say resetting flags"
flags =_FlagRegister(pPool.alloc())
ipRegister = pPool.alloc()

stackRegister = pPool.alloc()
adressRegister = pPool.alloc()

regRef1=pRefrence("REG_REF_1","1 11 -8")
regRef=regRef1
regRef2=pRefrence("REG_REF_2","1 11 -10")



AL=pPool.alloc()
BL=pPool.alloc()
CL=pPool.alloc()
DL=pPool.alloc()
AH=pPool.alloc()
BH=pPool.alloc()
CH=pPool.alloc()
DH=pPool.alloc()
