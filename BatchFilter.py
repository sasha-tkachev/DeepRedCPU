from pymclevel import TAG_List
from pymclevel import TAG_Byte
from pymclevel import TAG_Int
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Double
from pymclevel import TAG_String
from heapq import *
displayName = "Batch Command"
inputs=(
	("cmd","string"),
	("orderBy","string")
)
class CommandBlock:
	def __init__(self,tile,chunk,x,y,z):
		self.tile=tile
		self.chunk=chunk
		self.x=x
		self.y=y
		self.z=z
def perform(level, box, options):
	cmdBlocks=[]

	for (chunk, slices, point) in level.getChunkSlices(box):
		for t in chunk.TileEntities:
			x = t["x"].value
			y = t["y"].value
			z = t["z"].value
			
			key=x
			if options["orderBy"].lower()=="y":
				key=y
			if options["orderBy"].lower()=="z":
				key=z

			if x >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz and t["id"].value == "Control":
				
				heappush(cmdBlocks,(key,CommandBlock(t,chunk,x,y,z)))
				#t["Command"] = TAG_String(options["cmd"].format(i=index,X=x,Y=y,Z=z))
				#index+=1
				#chunk.dirty = True
	
	compileCommandBlocks(cmdBlocks,options["cmd"])			

def compileCommandBlocks(blocks,command):
	index=0
	while len(blocks)>0:
		block=heappop(blocks)[1]
		block.tile["Command"] = TAG_String(command.format(i=index,X=block.x,Y=block.y,Z=block.z))
		index+=1
		block.chunk.dirty = True
