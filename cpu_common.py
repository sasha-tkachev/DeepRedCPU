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
def msg(string):
	return "/say {}".format(string)

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
	def mv(self,dest):
		if not isinstance(dest,Pear):
			raise Exception("dest must be a pear")
		if not self.size > dest.size:
			raise Exception("the pear cannot be bigger then the destenation")
		return "/clone {} {} replace move".format(str(self.getOrigin),str(dest.dest))
	def get(self,dest):
		return self.clone(dest)
	def set(self,dest):
		if isinstance(dest, Pear):
			return dest.clone(self)
		#check if dest is actually a literal
		else:
			return Literal(dest).clone(self)
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
	
	def __call__(self,indirectTake=None):
		if self.size>1:
			raise Exception("you cannot call a pear that the size of it is bigger then 1")
		
		if indirectTake:
			return "/clone {0} {0} {1} replace move ".format(str(indirectTake),str(self.dest))
		return self.setTrue()
	def __str__(self):
		return str(self.dest)

class Literals:
	def byte(self,n):
		# n is number
		n=int(n)
		start = Point("37 11 26")
		column=int(n%8)
		row=int(n/8)
		selected=Pear(Point(37,start.y+row,start.z+column),8)
		return selected

	def char(self,c):
		if(isinstance(c,chr)):
			return Byte(ord(c))
		else :
			raise Exception(" c have to be a char")
	
	def __call__(self,v):
		if isinstance(v,int):
			return self.byte(v)
		elif isinstance(v,chr):
			return self.char(v)
		else:
			raise Exception("v is invalid literal")

	def OprandByte(self,cdu,n,order):
		return "/clone " +self.Byte(n).getOrigin()+" "+cdu.getUnpackedPear(order)

class Component:
	def __init__(self, invokeEnter):
		if not isinstance(invokeEnter, Pear):
			raise Exception("invokeEnter must be a pear")
		#pear with the isze of 1
		self.invokeEnter=invokeEnter
		self.subReturn=Pear(Point(invokeEnter.dest.x,invokeEnter.dest.y,invokeEnter.dest.z-1))
	def __call__(self,exit=None):
		toRet="/setblock "+str(self.invokeEnter)+" command_block 0 replace {Command:/setblock ~ ~-1 ~-1 command_block 0 replace {Command:"
		if exit ==None:
			print("WARNING no callback for call")
			return toRet +"/say subrutine is done, no follow-up}}"
		return toRet+"/setblock "+str(exit)+" redstone_block}}"
class Component1(Component):
	def __init__(self, invokeEnter,iNumberA,oResult,_proa,_proc):
		Component.__init__(self,invokeEnter)
		self.iNumberA=iNumberA
		self.oResult=oResult
		self._proa=_proa
		self._proc=_proc
		self.iValue=_proa
class Component2(Component1):
	def __init__(self, invokeEnter,iNumberA,iNumberB,oResult,_proa,_prob,_proc ):
		Component1.__init__(self, invokeEnter,iNumberA,oResult,_proa,_proc)
		self.iNumberB=iNumberB
		self._prob=_prob

class PearPool:
	def __init__(self,start,width,hight):
		if isinstance(start,str):
			start=Point(start)
		if not isinstance(start, Point):
			raise Exception("invalid start point")
		self.start=start
		self.width=width
		self.hight=hight
		self.curz=0
		self.cury=0
		self.slotCount=0
		self.tmp=self.alloc()
	def alloc(self,size=8):
		if size != 8:
			raise Exception("unimplamentd")
		self.curz+=1
		toRet=Pear(Point(self.start.x,self.start.y+self.cury,self.start.z+self.curz),size)
		if self.curz >= self.width:
			self.curz=0
			self.cury+=1
			if self.cury>=self.hight:
				raise Exception("ther is not enoth place for more slots")
		self.slotCount+=1
		return toRet
	#mainly for cmd blocks
	def safeAlloc(self,size=8):
		print("WARNING! SAFE ALLOC IS JUST LIKE ALLOC")
		return self.alloc(size)
	def tmpAlloc(self,size=8):
		print("WARNING TMP ALLOC USED")
		return self.tmp
class PortPool():

	JMP_X = 3
	JMP_Y = 4
	JMP_Z= -4
	def __init__(self,start,width,hight,length):
		self.slots =  []
		if not isinstance(start,Point):
			raise Exception("start must be a point")
		self.start=start
		self.width=width
		self.hight=hight
		self.length=length
		self.curX=0
		self.curY=0
		self.curZ=0
		self.slotCount=0
	def alloc(self, bind):

		if not isinstance(bind, Pear):
			raise Exception("bind must be a pear")
		
		self.slots.append(bind)
		self.curX+=1
		if  self.curX >= self.width:
			self.curX = 0
			self.curY +=1
		if  self.curY >= self.hight:
			self.curY=0
			self.curZ+=1
		if self.curZ >= self.length:
			raise Exception("ports depleated. we have {} ports allready".format(self.slotCount))
		self.slotCount+=1
		return Pear(Point(
			self.start.x + self.curX * PortPool.JMP_X,
			self.start.y + self.curY * PortPool.JMP_Y,
			self.start.z + self.curZ * PortPool.JMP_Z)
		)
	def count(self,x,y,z):
		return x+ y*self.width + z*self.hight
	def slot(self,i,j,k):
		try:
			print("for {} {} {} the slot is",i,j,k,self.count(i,j,k) )
			return self.slots[self.count(i,j,k)]()
		except IndexError:
			return "/say unallocated port"
	
portPool=PortPool(Point(29, 12, 3),6,4,2)
pPool = PearPool(Point(28 ,11, 41),3,16)
Literal=Literals()