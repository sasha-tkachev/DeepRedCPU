from cpu_component import Component
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
	def __call__(self,indirectTake):
		if self.size>1:
			raise Exception("you cannot call a pear that the size of it is bigger then 1")
		
		if indirectTake:
			return "/clone {0} {0} {1} replace move ".format(str(indirectTake),str(self.dest))
		return self.setTrue()
	
	def __str__(self):
		return str(self.dest)
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

class Group:
	
	pass
class Unit:

	pass

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


pPool = PearPool("0 0 0",50,1)
Literals=Literal()