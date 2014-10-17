import common
class CartPivot:
	def __init__(self,ID,spawnPosition):
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