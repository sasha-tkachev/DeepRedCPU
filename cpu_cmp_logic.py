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
