
from cpu_common import *
class Opcode(Component):
	def __init__(self,*args):
		self.subStart=args[0]
		invokeEnter=portPool.alloc(self.subStart)
		Component.__init__(self,invokeEnter)
		self.frames=args
		
		self.subReturn=Pear(Point(invokeEnter.x+1,invokeEnter.y,invokeEnter.z))
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
ROWS=[
	Point(28,12,19),
	Point(28,12,17),
	Point(28,12,11)
]
def f(row,index):
	s = ROWS[row]
	return Pear(Point(s.x+index,s.y,s.x))

MovRC =Opcode(
	f(1,0)
	)
MovRiM=Opcode(
	f(0,0),
	f(1,1)
	)
MovRdM=Opcode(
	f(0,1),
	f(1,2)
	)
PopR  =Opcode(
	f(0,2),
	f(2,4),
	f(1,4)
	)
MovMiR=Opcode(
	f(2,0)
	)
MovMdR=Opcode(
	f(2,1)
	)
MovRR =Opcode(
	f(0,5)
	)
PushC =Opcode(
	f(2,2),
	f(0,3),
	f(1,5)
	)
AddRC =Opcode(
	f(2,3),
	f(1,3)
	)
PushR =Opcode(
	f(2,5),
	f(0,4),
	f(1,6)
	)
