from cpu_component import Component
from cpu_ref import pRefrence
from cpu_common import pPool, Point, Pear


class _FlagRegister(Pear):
	def __init__(self,dest):
		regSize=8
		if isinstance(dest,Pear) and dest.size == regSize:
			self = dest
		elif isinstance(dest,Point):
			Pear.__init__(self,dest,regSize)
		else:
			raise Exception("dest must be a point or a pear with the size {}".format(regSize))
		
		self.carry=self.bit(0)
		self.pairity=self.bit(1)
		self.zero=self.bit(2)
		self.sign=self.bit(3)
		self.overflow=self.bit(4)

flags=_FlagRegister(pPool.alloc())
ipRegister = pPool.alloc()
stackRegister = pPool.alloc()
adressRegister = pPool.alloc()

regRef1=pRefrence("REG_REF_1","1 11 -8")
regRef=regRef1
regRef2=pRefrence("REG_REF_2","1 11 -10")