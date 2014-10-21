import common
import math
class CartPivot:
	def __init__(self,ID,spawnPosition):
		print("the the class of the spawnPosition is"+str(spawnPosition.__class__.__name__))
		if not isinstance(ID,str):
			raise Exception("ID must be string")
		if not isinstance(spawnPosition,common.Point):
			if isinstance(spawnPosition,str):
				spawnPosition= common.Point(spawnPosition)
			else:
				raise Exception("spawnPosition must be or a string inform of a point or a point ")
		self.ID=ID
		self.selector="@e[name={0}]".format(self.ID)
		self.spawnPosition=spawnPosition
	
	def spawn(self):
		return "/summon ArmorStand "+str(self.spawnPosition)+" {CustomName:\""+str(self.ID)+"\",NoGravity:1}"
	def kill(self):
		return "/kill @e[name="+str(self.ID)+"]"
	def signal(self,block="redstone_block"):
		return self.execute("/setblock ~ ~ ~ "+block)
	def Signal(self,block="redstone_block"):
		return self.signal(block)
	def execute(self,cmd):
		return "/execute {0} ~ ~ ~ {1}".format(self.selector,cmd)
	def Execute(self,cmd):
		return slef.execute(cmd)
	def clone(self,area,dest):
		if isinstance(dest,common.Pear):
			dest=dest.dest
		if isinstance(area,common.Pear):
			area=area.getOrigin()
		return self.execute("/clone {} {}").format(str(area),str(dest))
	def tp(self,direction):
		return "/tp @e[name="+self.ID+"] " + str(direction)
	def moveX(self, blocks):
		return "/tp @e[name="+self.ID+"] ~"+str(blocks)+" ~ ~"
	def moveY(self,blocks):
		return "/tp @e[name="+self.ID+"] ~ ~"+str(blocks)+" ~"
	def moveZ(self,blocks):
		return "/tp @e[name="+self.ID+"] ~ ~ ~"+str(blocks)
	def __str__():
		return ID
class pRefrence(CartPivot):
	def __init__(self,ID,spawnPosition):
		CartPivot.__init__(self,ID,spawnPosition)
		
	def origin(self, pear):
		return self.tp(pear.dest)
	def set(self,pear):
		return self.execute("/clone {} {}".format(str(pear.getOrigin()),"~ ~ ~"))
	def get(self,destPear):
		return self.execute("/clone ~ ~ ~ ~{} ~ ~ {}".format(destPear.size-1,destPear.dest))

class MatrixPivot(pRefrence):
	BASE=2
	def __init__(self,ID,spawnPosition,matrixSize=(16,16),matrixJump=(1,1)):
		pRefrence.__init__(self,ID,spawnPosition)
		if len(matrixSize) != len(matrixJump):
			raise Exception("jump and matrix sizes dont match")
		self.matrixSize=matrixSize
		self.jmp=matrixJump
		#hack
		self.logs=[]	
		
		for dementionSize in matrixSize:
			lg=math.log(dementionSize,MatrixPivot.BASE)
			self.logs.append(lg)
			if not lg.is_integer():
				raise Exception("matrix size is illigal")
	def moveByBit(self,bit):

		funtions= (self.moveX,self.moveY,self.moveZ)
		for demention,log in enumerate(self.logs):
			print("the demention is {} and the log of that is {}".format(demention,log))
			if bit < log:
				return funtions[demention](
					(MatrixPivot.BASE+self.jmp[demention]-1)**(bit-(demention*log)))