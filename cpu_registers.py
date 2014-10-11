from cpu_common import *
from cpu_component import *
from cpu_ref import *
from cpu_common import pPool


class _FlagRegister(Pear):
	def __init__(self,dest):
		Pear.__init__(self,dest,8)
		self.carry=self.bit(0)
		self.pairity=self.bit(1)
		self.zero=self.bit(2)
		self.sign=self.bit(3)
		self.overflow=self.bit(4)

flags=_FlagRegister(pPool.alloc())
ipRegister = pPool.alloc()
stackRegister = pPool.alloc()
adressRegister = pPool.alloc()
