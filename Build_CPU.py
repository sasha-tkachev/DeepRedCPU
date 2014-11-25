#search for command blocks, eval what is between the ^^
from pymclevel 			import TAG_List
from pymclevel 			import TAG_Byte
from pymclevel 			import TAG_Int
from pymclevel 			import TAG_Compound
from pymclevel 			import TAG_Short
from pymclevel 			import TAG_Double
from pymclevel 			import TAG_String
from common 			import *
from cpu_cmp_logic		import *
from cpu_cmp_calc		import *
from cpu_cmp_ram 		import Ram
from cpu_cmp_ram 		import tape
from cpu_cmp_cdu 		import Cdu
from cpu_ref 			import *
from cpu_registers 		import *
from keyboard 			import keyboard
import cpu_opcodes
import program_loader
import json
from misc import chatHub
displayName = "Build CPU"
print(" {} ports and {} pears allocated ".format(portPool.slotCount,pPool.slotCount))
print(len(CartPivot.used),"carts are being used")
p=Cdu.interpreter
locals().update(cpu_opcodes.opcodes) 
locals().update(generalPurpase)

def perform(level, box, options):
	for i,row in enumerate(tape):
		if isinstance(row, int):
			byte='{0:08b}'.format(row)
			loc=None
			for bnum,bit in enumerate(byte):
				z=int(i%16)
				y=int(i/16)
				loc=tape.corner+Point(7-bnum,y,z)
				print(str(loc))
				if(bit=='0'):
					level.setBlockAt(loc.x,loc.y,loc.z, 80)
				else:
					level.setBlockAt(loc.x,loc.y,loc.z,152)
				level.getChunk(loc.x / 16, loc.z / 16).dirty = True
		elif isinstance(row, list):
			if len(row)!=8:
				raise Exception("[Image File Error] opcode byte size is not 8 bits long")
			for bnum, bit in enumerate(row):
				tape[i][bnum]=parseCommand(bit)
	for (chunk, slices, point) in level.getChunkSlices(box):
		for t in chunk.TileEntities:
			_x = t["x"].value
			_y = t["y"].value
			_z = t["z"].value
			
			if _x >= box.minx and _x < box.maxx and _y >= box.miny and _y < box.maxy and _z >= box.minz and _z < box.maxz and t["id"].value == "Control":
				command = t["Command"].value
				t["Command"] = TAG_String(parseCommand(command))
				chunk.dirty = True
def parseCommand(command):
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
				
				try:
					a=str(eval(toeval))
				except Exception as exp:
					a="/say [ERROR] "+str(exp)
				result+=a
				print("    >"+a)
				toeval=""
			else:
				toeval+=char
		i=i+1

	return result	