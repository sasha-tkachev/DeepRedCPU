from cpu_common import *
from cpu_component import *
from cpu_ref import *
class CartPivot:	
	def __init__(self,ID,spawnPosition):
		if not(isinstance(ID,str)):
			raise Exception("ID must be string")
		if not(isinstance(spawnPosition,Point)):
			if isinstance(spawnPosition,str):
				spawnPosition=Point(spawnPosition)
			else:
				raise Exception("spawnPosition must be or a string inform of a point or a point ")
		self.ID=ID
		self.selector="@e[name={0}]".format(self.ID)
		self.spawnPosition=spawnPosition
	def Spawn(self):
		return "/summon ArmorStand "+str(self.spawnPosition)+" {CustomName:\""+str(self.ID)+"\",NoGravity:1}"
	def spawn(self):
		return self.Spawn()
	def Kill(self):
		return "/kill @e[name="+str(self.ID)+"]"
	def kill(self):
		return self.Kill()
	def Signal(self,block="redstone_block"):
		return "/execute @e[name="+str(self.ID)+"] ~ ~ ~ /setblock ~ ~ ~ "+block
	def signal(self,block="redstone_block"):
		return self.Signal(block)
	def Execute(self,cmd):
		return "/execute {0} ~ ~ ~ {1}".format(self.selector,cmd)
	def clone(self,area,dest):
		if isinstance(dest,Pear):
			dest=dest.dest
		if isinstance(area,Pear):
			area=area.getOrigin()
		return self.Execute("/clone {} {}").format(str(area),str(dest))
	def Tp(self,direction):
		return "/tp @e[name="+self.ID+"] "+direction
	def tp(self,direction):
		return self.Tp(direction)
	def MoveX(self, blocks):
		return "/tp @e[name="+self.ID+"] ~"+str(blocks)+" ~ ~"
	def MoveY(self,blocks):
		return "/tp @e[name="+self.ID+"] ~ ~"+str(blocks)+" ~"
	def MoveZ(self,blocks):
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
