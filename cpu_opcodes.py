from cpu_common import *
from cpu_main import root
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

data =json.loads(open(root.data+"opcodes.json").read())[1]
rows=data.rows
opcodes=data.opcodes
for codeName , frames in opcodes.iteritems():
	pList=[]
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
				raise Exception("invalid frame syntax")
		else:
			raise Exception("invalid frame syntax")
		pList.append(retPear)
	opcodes[codeName]=Opcode(pList)
 