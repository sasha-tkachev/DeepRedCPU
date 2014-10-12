from cpu_common import *
class Component:
	def __init__(self, invokeEnter):
		#pear with the isze of 1
		self.invokeEnter=invokeEnter
	def __call__(self,exit):
		return "/setblock "+str(self.invokeEnter)+" command_block 0 replace {Command:/setblock "+str(exit)+" redstone_block}"
class Component1(Component):
	def __init__(self, invokeEnter,iNumberA,oResult,_proa,_proc):
		Component.__init__(self,invokeEnter)
		self.iNumberA=iNumberA
		self.oResult=oResult
		self._proa=_proa
		self._proc=_proc
		self.iValue=_proa
class Component2(Component1):
	def __init__(self, invokeEnteriNumberA,iNumberB,oResult,_proa,_prob,_proc ):
		Component1.__init__(self, invokeEnter,iNumberA,oResult,_proa,_proc)
		self.iNumberB=iNumberB
		self._prob=_prob
class PortPool():
	JMP_X = 5
	JMP_Y = 5
	JMP_Z = 5
	def __init__(self,start,width,hight,length):
		if not isinstance(start,Point):
			raise Exception("start must be a point")
		self.start=start
		self.width=width
		self.hight=hight
		self.length=length
		self.curX=0
		self.curY=0
		self.curZ=0
	def alloc(self):
		self.curX+=1
		if  self.curX >= self.width:
			self.curX = 0
			self.curY +=1
		if  self.curY >= self.hight:
			self.curY = 0
			self.curZ +=1
		if self.curZ >= self.length:
			raise Exception("port pool is depleated")
		return Point(self.start.x+self.curX*JMP_X,self.start.y+self.curY*JMP_Y,self.start.y+self.curZ*JMP_Z)

portPool=PortPool(Point(0,20,0)),30,30,30)