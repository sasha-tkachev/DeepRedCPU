from cpu_common import *
from cpu_component import *
from cpu_ref import *
class ADDER(Component):
	class Summer:
		def __init__(self,pivot,cOut,proPear):
			self.pivot=pivot
			self.cOut=cOut
			self.proPear=proPear
		def addOne(self):
			return self.pivot.MoveZ(-1)
		def subOne(self):
			return self.pivot.MoveZ(1)
		def shut(self):
			return self.pivot.kill()
		def start(self):
			return self.pivot.spawn()
		def carry(self):
			print str(self.cOut)
			return self.cOut.addOne()
		def sum(self):
			return self.proPear.setTrue()
		def call(self):
			return self.pivot.signal()
		def __str__(self):
			return "cart:{} cOut:{} pear:{}".format(self.pivot.ID,self.cOut,self.proPear)
	def __init__(self,peara,pearb,iNumberA,iNumberB,oResult,_proa,_prob,_proc,sStart,caller,stage2,stage3,stage4):
		Component.__init__(self,peara,pearb)
		self.iNumberB=iNumberB
		self.iNumberA=iNumberA
		self.oResult=oResult
		self._proa=_proa
		self._prob=_prob
		self._proc=_proc
		if isinstance(sStart,str):
			sStart=Point(sStart)
		self.sStart=sStart
		n=self.oResult.size
		self.summers=self.createSummers([None]*n,n-1,None)
		self.stage3=stage3
		self.stage2=stage2
		self.stage4=stage4
		self.caller=caller
	def createSummers(self,l,i,carry):
		if i <0:
			return l
		toAppend=ADDER.Summer(
			CartPivot(
				"ADDER_SUM_"+str(i),
				Point(
					self.sStart.x+i,
					self.sStart.y,
					self.sStart.z
				)
			),
			carry,
			self._proc.bit(i)
		)
		l[i]=(toAppend)
		return self.createSummers(l,i-1,toAppend)
class INCREASER(Component):
	def __init__(self,pa,pb,inp,out,_pro,pivot):
		Component.__init__(self,pa,pb);
		self.iValue=inp
		self.oResult=out
		self._pro=_pro
		self.pivot=pivot
class SHIFTER(Component):
	def __init__(self,peara,pearb,result,value,_bitpro,isReversed=False):
		Component.__init__(self,peara,pearb)
		self.oResult=result
		self.iValue=value
		self._bitpro=_bitpro
		self._reversed=isReversed
	def shiftBit(self,i):
		if self._reversed:
			return self.oResult.bit((i+1)%8).setTrue()
		else:
			return self.oResult.bit((i-1)%8).setTrue()	

