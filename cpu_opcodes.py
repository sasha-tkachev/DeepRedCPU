from common import *
import json
class Opcode(Component):
	def __init__(self,args):
		self.subStart=args[0]
		invokeEnter=portPool.alloc(self.subStart)
		Component.__init__(self,invokeEnter)
		self.frames=args
		
		self.end=self.subReturn
	def ret(self,take='bottom'):
		take = {
			'south': '~ ~ ~1' , \
			'north': '~ ~ ~-1', \
			'east':	 '~1 ~ ~' , \
			'west':  '~-1 ~ ~', \
			'bottom':'~ ~-1 ~', \
			'up':    '~ ~1 ~' , \
			}[take]
		return self.subReturn(take)
	def __getitem__(self,index):
		return self.frames[index]

data =json.loads(open("E:/Games/Minecraft/mcedit/MCEdit-0.1.7.1.win-amd64/filters/data/opcodes.json","r").read())
rows=data["rows"]
opcodes=data["opcodes"]
#list made for outer use 
codes=list()

for codeName,frames in opcodes.items():
	pList=[]
	print(codeName+" = ")
	for frame in frames:
		retPear=None
		if isinstance(frame,list):
			rowStart=rows[frame[0]]
			retPear=Pear(Point(
					rowStart[0]+frame[1],
					rowStart[1],
					rowStart[2],
					))
		elif isinstance(frame,dict):
			try:
				d=frame["Pear"]["dest"]
				retPear=Pear(Point(d[0],d[1],d[2]),frame["Pear"]["size"])
			except KeyError:
				raise Exception("invalid frame syntax expecting ")
		else:
			raise Exception("invalid frame syntax")
		print('  '+str(retPear))
		pList.append(retPear)
	op=Opcode(pList)
	opcodes[codeName]=op
	codes.append((codeName,op))
def f(row,i):
	return Pear(Point(rows[row][0]+i,rows[row][1],rows[row][2]))
