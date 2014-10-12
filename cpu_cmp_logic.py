from cpu_common import *
from cpu_component import *
from cpu_ref import *
class XORER(Component2):
	def __init__(self,peara,pearb,iNumberA,iNumberB,oResult,_pora,_prob,_proc,banka,bankb,_test,_testRecall):
		Component2.__init__(self,peara,pearb,iNumberA,iNumberB,oResult,_pora,_prob,_proc)
		self.bankb=bankb
		self.banka=banka
		self._test=_test
		self._testRecall=_testRecall
	def resetPros(self):
		return "/fill {} {} {}".format(str(self._proa.dest),str(self._prob.getEndOfOrigin()),Pear.resetBlock)
class ORER(Component2):
	def __init__(self, invokeEnter, invokeExitBlock,iNumberA,iNumberB,oResult,_proa,_prob,_proc ,_cont,_end):
		Component2.__init__(self, invokeEnter, invokeExitBlock,iNumberA,iNumberB,oResult,_proa,_prob,_proc )
		self._end=_end
		self._cont=_cont
class INVERTER(Component):
	def __init__(self,pa,pb,inp,outp,_pro):
		Component.__init__(self,pa,pb);
		self.iValue=inp
		self.oResult=outp
		self._pro=_pro
	def invertBit(self,n):
		return self.oResult.bit(n).setFalse()

Inverter=INVERTER(
		Pear("38 15 19"),
		Pear("41 14 19"),
		Pear("1 11 19",8),
		Pear("1 11 20",8),
		Pear("37 11 19",8),
		)
Orer=ORER(
	Pear("44 14 19"),Pear("44 14 14"),#invokes
	Pear("1 11 21",8),Pear("1 11 22",8),Pear("1 11 23",8),#interface
	Pear("37 15 15",8),Pear("37 14 16",8),Pear("37 15 16",8),#internalMem
	Pear("37 15 14"),Pear("37 21 18")#internalPointers
	)
Xorer=XORER(
	Pear("43 18 18"),Pear("42 17 18"),#invokes
	Pear("1 11 24",8),Pear("1 11 25",8),Pear("1 11 26",8),#interfaces
	Pear("37 17 20",8),Pear("37 19 20",8),Pear("37 18 20",8),#internalSlots
	Area("44 17 19","44 19 19"),Area("43 17 19","43 19 19"),#banks
	Pear("37 18 23"),#_test
	Pear("38 14 3"),#testrecall
	)