from common import *
from cpu_opcodes import *
from cpu_ref import *

class NEGATOR(Opcode):
	def __init__(self,iValue,oResult,a1,a2,a3):
		Opcode.__init__(self,[a1,a2,a3])
		self.iValue=iValue
		self.oResult=oResult
class XORER(Component2):
	def __init__(self,peara,iNumberA,iNumberB,oResult,_proa,_prob,_proc,bank):
		Component2.__init__(self,peara,iNumberA,iNumberB,oResult,_proa,_prob,_proc)
		if not isinstance(bank,Pear):
			raise Exception("bank must be pear")
		self.bank = bank
	def action(self,i): 
		p1=self.bank.bit(i)
		print("the size of p1 is "+str(p1.size))
		p2=self._proc.bit(i)
		print("the size of p2 is "+str(p2.size))
		return p1.mv(p2)
	def inputReset():
		return "/fill {} {} {}".format(
			str(self._proa.dest),
			str(self._prob.getEndOfOrigin()),
			Pear.resetBlock)
	def bankReset():
		return "/fill {} {} {}".format(
			str(self.bank.dest),
			str(self._proc.getEndOfOrigin()),
			Pear.resetBlock)
class ORER(Component2):
	def __init__(self, invokeEnter,iNumberA,iNumberB,oResult,_proa,_prob,_proc ,_cont,_end):
		Component2.__init__(self,invokeEnter,iNumberA,iNumberB,oResult,_proa,_prob,_proc )
		self._end=_end
		self._cont=_cont
class INVERTER(Component):
	def __init__(self,pa,inp,outp,_pro):
		Component.__init__(self,pa);
		self.iValue=inp
		self.oResult=outp
		self._pro=_pro
	def invertBit(self,n):
		return self.oResult.bit(n).setFalse()

Inverter=INVERTER(
		Pear("37 14 21"),
		pPool.alloc(),
		pPool.alloc(),
		Pear("37 11 21",8)
		)
Orer=ORER(
	Pear("44 14 19"),#invokes
	pPool.alloc(),pPool.alloc(),pPool.alloc(),#interface
	Pear("37 15 15",8),Pear("37 14 16",8),Pear("37 15 16",8),#internalMem
	Pear("37 15 14"),Pear("37 21 18")#internalPointers
	)
Xorer=XORER(
	Pear("37 15 21"),#enter
	pPool.alloc(),pPool.alloc(),pPool.alloc(),#interfaces
	Pear("37 15 22",8),Pear("37 15 23",8),Pear("37 15 24",8),#internalSlots
	Pear("37 14 24",8)#bank
	)

Negator = NEGATOR(
	pPool.alloc(),
	pPool.alloc(),
	f(0,6),
	f(0,7),
	f(4,0)
	)
