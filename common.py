from cpu_ref import *

import math
def Clone(peara,pearb,way="replace"):
	wayDict={"replace":True,"replace move":True}
	if 	isinstance(peara,Pear) and isinstance(pearb,Pear) and (pearb.size == peara.size ):
		toRet=""
		if peara.size>1:
			print("we got here.")
			toRet+= "/clone {} {}".format(str(peara.getOrigin()),str(pearb.dest))
		elif peara.size==1:
			toRet+= "/clone {0} {0} {1}".format(str(peara.dest),str(pearb.dest))
		try:
			if not wayDict[way]:
				msg='clone "{}" way is currently inactive. the active ways are: '.format(way)
				for wayName,isActive in wayDict.items():
					if isActive:
						msg+=', '+wayName
				raise Exception(msg)
		except KeyError:
			msg = 'clone way "{}" is invalid please. the ways are: '
			for name, isActive in wayDict.items():
				msg+=', '+name
			raise Exception(msg)
		return toRet +' '+ way
	elif isinstance(peara,Pear) and isinstance(pearb,pRefrence):
		return pearb.set(peara)
	elif isinstance(peara,pRefrence) and isinstance(pearb,Pear):
		return peara.set(pearb)
	raise Exception("the 2 arguments must be pears with a same size, the size of the two of the pears are {} {} and the classes are {} {}".format(peara.size,pearb.size,peara.__class__.__name__,pearb.__class__.__name__))
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
	def __getitem__(self,i):
		if i==0:
			return self.x
		if i==1:
			return self.y
		return self.z
	def __setitem__(self,i,value):
		if i==0:
			 self.x=value
		elif i==1:
			self.y = value
		else:
			self.z =value
	def __add__(self,other):
		return Point(self.x+other[0],self.y+other[1],self.z+other[2])
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
	def clone(self,pear,way="replace"):
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
		if self.size > dest.size:
			raise Exception("the pear cannot be bigger then the destenation")
		return "/clone {} {} {} replace move".format(str(self.dest),str(self.getOrigin()),str(dest.dest))
	def get(self,dest):
		return self.clone(dest)
	def set(self,dest):
		if isinstance(dest, Pear):
			return dest.clone(self)
		#check if dest is actually a literal
		if isinstance(dest, str) and len(dest)>1:
			return "/setblock {} {}".format(str(self.dest),dest)
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
		return Pear(retpoint,1)	
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
			try:
				indirectTake = {
					'south': '~ ~ ~1' , \
					'north': '~ ~ ~-1', \
					'east':	 '~1 ~ ~' , \
					'west':  '~-1 ~ ~', \
					'bottom':'~ ~-1 ~', \
					'up':    '~ ~1 ~' , \
					}[indirectTake]
			except:
				pass
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
		row=int(math.log(n,8))
		selected=Pear(Point(37,start.y+row,start.z+column),8)
		return selected
	def char(self,c):
		if(isinstance(c,str)):
			return self.byte(ord(c))
		else :
			raise Exception(" c have to be a char")
	def OprandByte(self,cdu,n,order):
		return "/clone " +self.Byte(n).getOrigin()+" "+cdu.getUnpackedPear(order)
	def __call__(self,v):
		if isinstance(v,int):
			return self.byte(v)
		elif isinstance(v,chr):
			return self.char(v)
		else:
			raise Exception("v is invalid literal")

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
			return toRet +"/say subrutine is done }}"
		if isinstance(exit,str):
			return toRet+exit+" }}"
		return toRet+exit()+"}}"
class LinkedComponent(Component):
	def __init__(self,invokeEnter):
		invokeEnter=portPool.alloc(invokeEnter)
		Component.__init__(self,invokeEnter)
class Component1(LinkedComponent):
	def __init__(self, invokeEnter,iNumberA,oResult,_proa,_proc):
		LinkedComponent.__init__(self,invokeEnter)
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
		self.cury+=1
		toRet=Pear(Point(self.start.x,self.start.y+self.cury,self.start.z+self.curz),size)
		if self.cury >= self.hight:
			self.cury=0
			self.curz+=1
			if self.curz>=self.width:
				raise Exception("ther is not enoth place for more slots")
		self.slotCount+=1
		return toRet
	def safeAlloc(self,size=8):
		print("WARNING! SAFE ALLOC IS JUST LIKE ALLOC")
		return self.alloc(size)
	def tmpAlloc(self,size=8):
		print("WARNING TMP ALLOC USED")
		return self.tmp
class PortPool():
	indexForm ="{},{},{}"
	JMP_X = 3
	JMP_Y = 4
	JMP_Z = -4
	def __init__(self,start,width,hight,length):
		self.slots =  dict()
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
		
		self.slots[PortPool.indexForm.format(self.curX,self.curY,self.curZ)]=bind
		toRet=Pear(Point(
			self.start.x + self.curX * PortPool.JMP_X,
			self.start.y + self.curY * PortPool.JMP_Y,
			self.start.z + self.curZ * PortPool.JMP_Z)
		)
		self.slotCount+=1
		self.curX+=1
		if  self.curX >= self.width:
			self.curX = 0
			self.curY +=1
		if  self.curY >= self.hight:
			self.curY=0
			self.curZ+=1
		if self.curZ >= self.length:
			raise Exception("ports depleated. we have {} ports allready".format(self.slotCount))
		
		return toRet
	def slot(self,i,j,k):
		try:
			st=PortPool.indexForm.format(i,j,k)
			bind=self.slots[st]()
			print("the bind of the slot {} is {}".format(st,bind))
			return bind
		except KeyError:
			return "/say unallocated port"
	
portPool=PortPool(Point(29, 12, 22),3,4,4)
pPool = PearPool(Point(28 ,11, 41),4,15)
Literal=Literals()