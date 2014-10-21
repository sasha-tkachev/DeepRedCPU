from common import *
from cpu_ref import *
from cpu_opcodes import *
print("what")
class INCREASER(LinkedComponent):
	def __init__(self,enter,iValue,oResult,_pro,resRef,final):
		LinkedComponent.__init__(self,enter);
		self.iValue=iValue
		self.oResult=oResult
		self._pro=_pro
		self.resRef=resRef
		self.final=final
	def action(self,index):
		if index < 4 :
			return self.resRef.moveZ(2**index)
		index-=4
		return self.resRef.moveY(2**index)

class ADDER(LinkedComponent):
	class Summer:
		def __init__(self,pivot,cOut,proPear):
			self.pivot=pivot
			self.cOut=cOut
			self.proPear=proPear
		def addOne(self):
			return self.pivot.moveZ(-1)
		def subOne(self):
			return self.pivot.moveZ(1)
		def shut(self):
			return self.pivot.kill()
		def start(self):
			return self.pivot.spawn()
		def carry(self):
			print(str(self.cOut))
			return self.cOut.addOne()
		def sum(self):
			return self.proPear.setTrue()
		def __call__(self):
			return self.pivot.signal()
		def __str__(self):
			return "cart:{} cOut:{} pear:{}".format(self.pivot.ID,self.cOut,self.proPear)
	def __init__(self,peara,iNumberA,iNumberB,oResult,_proa,_prob,_proc,sStart,caller,stage2,stage3,stage4):
		LinkedComponent.__init__(self,peara)
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
		
		def foo():
			a=self.caller
			return "/summon MinecartRideable "+str(a.spawnPosition)+" {CustomName:\""+str(a.ID)+"\",NoGravity:1}"
		self.caller.spawn=foo
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
class SHIFTER(LinkedComponent):
	def __init__(self,peara,result,value,_pro,isRight=False):
		LinkedComponent.__init__(self,peara)
		self.oResult=result
		self.iValue=value
		self._pro=_pro
		self._reversed=isRight
	def shiftBit(self,i):
		if self._reversed:
			return self.oResult.bit((i+1)%8).setTrue()
		else:
			return self.oResult.bit((i-1)%8).setTrue()	

Adder=ADDER(
		Pear(Point("37 13 7")),#invoke enter
		pPool.alloc(),#inumba
		pPool.alloc(),#inumberb
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
		Pear("37 14 23"),
		pPool.alloc(),
		pPool.alloc(),
		Pear("37 11 23",8),
		pRefrence(
			"INCREASER_PIVOT",
			Point("37 11 27"),
			),
			f(5,2)
		)
Decreaser=INCREASER(
		Pear("37 14 22"),
		pPool.alloc(),
		pPool.alloc(),
		Pear("37 11 22",8),
		pRefrence(
			"DECREASER_PIVOT",
			Point("37 11 25")
			),
		f(5,3)
		)
ShifterLeft=SHIFTER(
		Pear("37 15 20"),
		pPool.alloc(),
		pPool.alloc(),
		Pear("37 14 18",8),
		False
		)
ShifterRight=SHIFTER(
		Pear("37 15 19"),
		pPool.alloc(),
		pPool.alloc(),
		Pear("37 11 18",8),
		True
		)