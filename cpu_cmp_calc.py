'''from cpu_common import *
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

Adder=ADDER(
		Pear(Point("37 14 9")),#invoke enter
		Pear(Point("44 14 6")),#invoke exit
		Pear("1 11 6",8),#inumba
		Pear("1 11 7",8),#inumberb
		Pear("1 11 8",8),#oResultt
		Pear("37 14 12",8),#_proa
		Pear("37 14 11",8),#_prob
		Pear("37 14 10",8),#_proc
		Point("37 12 16"),#carts
		CartPivot("ADDER_CALLER",Point("37 11 8")),#caller
		Pear("37 13 7"),#stage2c
		Pear("37 11 11"),#stage3
		Pear("37 13 6"),#stage4
		)
Increaser=INCREASER(
		Pear("40 15 23"),
		Pear("43 14 23"),
		Pear("1 11 15",8),
		Pear("1 11 16",8),
		Pear("37 11 23",8),
		CartPivot(
			"INCREASER_PIVOT",
			Point("37 11 27"),
			),
		)
Decreaser=INCREASER(
	Pear("40 15 21"),
	Pear("43 14 21"),
	Pear("1 11 17",8),
	Pear("1 11 18",8),
	Pear("37 11 21",8),
	CartPivot(
		"DECREASER_PIVOT",
		Point("37 11 25")
		),
	)
Shifter=SHIFTER(
		Pear("16 14 14"),
		Pear("19 14 14"),
		Pear("1 11 11",8),
		Pear("1 11 10",8),
		Pear("14 11 14",8),
		False
		)
DeShifter=SHIFTER(
		Pear("16 14 12"),
		Pear("19 14 12"),
		Pear("1 11 13",8),
		Pear("1 11 12",8),
		Pear("14 11 12",8),
		True
		)'''