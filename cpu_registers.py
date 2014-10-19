
from cpu_ref import pRefrence
from common import pPool, Point, Pear
import misc

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
	def aluReset(self):
		return "/say resetting flags"
flags =_FlagRegister(pPool.alloc())
ipRegister = pPool.alloc()

stackRegister = pPool.alloc()
adressRegister = pPool.alloc()


regRef1=pRefrence("REG_REF_1","1 11 -8")
regRef=regRef1
regRef2=pRefrence("REG_REF_2","1 11 -10")

generalPurpase={"AL":pPool.alloc(),"AH":pPool.alloc(),"BL":pPool.alloc(),"BH":pPool.alloc(),"CL":pPool.alloc(),"CH":pPool.alloc(),"DL":pPool.alloc(),"DH":pPool.alloc()}
gp=generalPurpase
def makePair(name,ref):
	mk=misc.chatHub.makeLink
	mk("  "+name+'L',ref.origin(gp[name+'L']))
	mk("  "+name+'H\n',ref.origin(gp[name+'H']))
misc.chatHub.makeLink("\n[Pointer A]\n",regRef1.spawn())
makePair('A',regRef1)
makePair('B',regRef1)
makePair('C',regRef1)
makePair('D',regRef1)
misc.chatHub.makeLink("[Pointer B]\n",regRef2.spawn())
makePair('A',regRef2)
makePair('B',regRef2)
makePair('C',regRef2)
makePair('D',regRef2)
