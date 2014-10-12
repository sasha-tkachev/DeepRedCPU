from cpu_ref import *
def Clone(peara,pearb):
	if 	isinstance(peara,Pear) and isinstance(pearb,Pear) and pearb.size == peara.size :
		return "/clone "+str(peara.getOrigin())+" "+str(pearb);
	elif isinstance(peara,Pear) and isinstance(pearb,pRefrence):
		return pearb.set(peara)
	elif isinstance(peara,pRefrence) and isinstance(pearb,Pear):
		return peara.set(pearb)
	raise Exception("the 2 arguments must be pears with a same size")
def Fill(peara,content):

	return "/fill {0} {1}".format(peara.getOrigin(),content)
class Group:
	pass
class Unit:
	pass

class Point:
	def __init__(self, inp,y=None,z=None):
		if isinstance(inp, str):
			cords=list()
			tmp=""
			i = 0
			till=len(inp)
			while i<till:
				c=inp[i]
				if c== ' ':
					cords.append(int(float(tmp)))
					tmp=""
				else:
				 	tmp=tmp+c
			 	i+=1
		 	cords.append(int(float(tmp)))
		 	self.x=cords[0]
		 	self.y=cords[1]
		 	self.z=cords[2]
	 	if isinstance(inp, int):
	 		self.x=inp
	 		self.y=y
	 		self.z=z
	def rel(self,point):
		return Point(
			self.x+point.x,
			self.y+point.y,
			self.z+point.z
			)
 	def __str__(self):
 		return str(self.x)+" "+str(self.y)+" "+str(self.z)
class Area:

	def __init__(self,p1,p2):
		'''if isinstance(p1,str):
			p1=Point(p1)

		if isinstance(p2,str):
			p2=Point(p2)
		'''
		self.p1=p1
		self.p2=p2
	def testForArea(self,areab):
		return "/testforblocks {} {}".format(str(self),str(areab.p1))
	def __str__(self):
		return "{} {}".format(str(self.p1),str(self.p2))
class Pear:
	resetBlock="snow"
	def getOrigin(self):
		if self.size>1:
			return str(self.dest)+" "+str(self.dest.x+self.size-1)+" "+str(self.dest.y)+" "+str(self.dest.z)
		else:
			return str(self.dest)
	def getEndOfOrigin(self):
		return str(self.dest.x+self.size-1)+" "+str(self.dest.y)+" "+str(self.dest.z)

	def bit(self, bitID):
		retpoint = Point( 
			self.dest.x + bitID,
			self.dest.y,
			self.dest.z
			)
		return Pear(retpoint)	
	def getSubPear(self,rangeStart,rangeEnd=None):
		if rangeEnd==None:
			rangeEnd=rangeStart
			rangeStart=0
		rangeSize = rangeEnd - rangeStart
		if rangeSize<0 or rangeStart<0 or rangeEnd > self.size:
			raise Exception("invalid range")
		retpoint = Point( 
			self.dest.x + rangeStart,
			self.dest.y,
			self.dest.z
			)
		return Pear(retpoint, rangeSize)
	
	def __init__(self, dest, size=1):
		if isinstance(dest,str):
			dest=Point(dest)
		if size>0:
			self.dest=dest
			self.size=size
	
	def fill(self,blocks):
		cmd="fill"
		if self.size == 1:
			cmd="setblock"
		return "/{} {} {}".format(cmd,str(self.getOrigin()),blocks)
	def clone(self,pear):
		return Clone(self,pear)
	def setTrue(self):
		return self.fill("redstone_block")
	def setFalse(self):
		return self.fill(self.resetBlock)
	def Reset(self):
		return self.setFalse()	
	def __call__(self,indirectTake=None):
		if self.size>1:
			raise Exception("you cannot call a pear that the size of it is bigger then 1")
		
		if indirectTake:
			return "/clone {0} {0} {1} replace move ".format(str(indirectTake),str(self.dest))
		return self.setTrue()
	
	def __str__(self):
		return str(self.dest)

class Literal:
	def Byte(self,n):
		# n is number
		n=int(n)
		start = Point("37 11 26")
		column=int(n%8)
		row=int(n/8)
		selected=Pear(Point(37,start.y+row,start.z+column),8)
		return selected

	def Char(self,c):
		if(isinstance(c,chr)):
			return Byte(ord(c))
		
	def OprandByte(self,cdu,n,order):
		return "/clone " +self.Byte(n).getOrigin()+" "+cdu.getUnpackedPear(order)

class Component:
	def __init__(self, invokeEnter):
		if not isinstance(invokeEnter, Pear)
			raise Exception("invokeEnter must be a pear")
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

class PearPool:
	def __init__(self,start,maxWidth,maxHight):
		if isinstance(start,str):
			start=Point(start)
		if not isinstance(start, Point):
			raise Exception("invalid start point")
		self.start=start
		self.maxWidth=maxWidth
		self.maxHight=maxHight
		self.curx=0
		self.cury=0
	def alloc(self,size=8):
		if size != 8:
			raise Exception("unimplamentd")
		self.curx+=1
		if self.curx > self.maxWidth:
			self.curx=0
			self.cury+=1
			if self.cury>self.maxHight:
				raise Exception("ther is not enoth place for more slots")
		return Pear(Point(self.start.x+self.curx,self.start.x+self.cury,self.start.z),size)
	#mainly for cmd blocks
	def safeAlloc(self,size=8):
		raise Exception("unimplamentd")
class PortPool():
	JMP_X = 4
	JMP_Y = 3
	def __init__(self,start,width,hight):
		self.slots =   [ [None] * hight ] * width
		if not isinstance(start,Point):
			raise Exception("start must be a point")
		self.start=start
		self.width=width
		self.hight=hight
		self.curX=0
		self.curY=0
	def alloc(self, bind):
		if not isinstance(bind, Pear):
			raise Exception("bind must be a pear")

		self.curX+=1
		if  self.curX >= self.width:
			self.curX = 0
			self.curY +=1
		if  self.curY >= self.hight:
			raise Exception("ports depleated")
		
		self.slots[self.curX][self.curY] = bind()
		return Pear(Point(
			self.start.x + self.curX * PortPool.JMP_X,
			self.start.y + self.curY * PortPool.JMP_Y,
			self.start.z)
		)	
	def slot(self,i,j):
		return self.slots[i][j]
portPool=PortPool(Point(30, 12, 4),4,4)
pPool = PearPool(Point(28 ,11, 41),2,16)
Literals=Literal()