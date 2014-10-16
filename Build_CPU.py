#search for command blocks, eval what is between the ^^
from pymclevel 			import TAG_List
from pymclevel 			import TAG_Byte
from pymclevel 			import TAG_Int
from pymclevel 			import TAG_Compound
from pymclevel 			import TAG_Short
from pymclevel 			import TAG_Double
from pymclevel 			import TAG_String
from cpu_common 		import *
from cpu_cmp_logic		import *
from cpu_cmp_calc		import *
from cpu_cmp_ram 		import Ram
from cpu_cmp_cdu 		import Cdu
from cpu_ref 			import *
from cpu_registers 		import *
import cpu_opcodes

displayName = "Build CPU"
print(" {} ports and {} pears allocated ".format(portPool.slotCount,pPool.slotCount))
def perform(level, box, options):
	locals().update(cpu_opcodes.opcodes)
	for (chunk, slices, point) in level.getChunkSlices(box):
		for t in chunk.TileEntities:
			_x = t["x"].value
			_y = t["y"].value
			_z = t["z"].value
			
			if _x >= box.minx and _x < box.maxx and _y >= box.miny and _y < box.maxy and _z >= box.minz and _z < box.maxz and t["id"].value == "Control":
				command = t["Command"].value
				command=command.replace("/say `","`")
				
				#print("[parsing] "+command)
				
				i = 0
				till=len(command)

				toeval=""
				result=""

				flag=True
				alert='`'
				while i<till:
					char =command[i]
					if flag:
						if char==alert:
							flag=False
						else:
							result+=char
					else:
						if char==alert:
							flag=True
							print ("[parsing] "+toeval)
							a=str(eval(toeval))
							result+=a
							print("    >"+a)
							toeval=""
						else:
							toeval+=char
					i=i+1

					
				t["Command"] = TAG_String(result)
				
				chunk.dirty = True
