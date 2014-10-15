
from cpu_common import *
class Opcode(Component):
	def __init__(self,*args):
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
ROWS=[
	Point(28,12,19),
	Point(28,12,17),
	Point(28,12,10),
	Point(28,12,15),
	Point(28,12,13),
	Point(28,12,7),
	Point(28,17,17),
	]
def f(row,index):
	s = ROWS[row]
	return Pear(Point(s.x+index,s.y,s.z))

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
AddRR =Opcode(
	f(2,6),
	f(1,7)
	)
PushR =Opcode(
	f(2,5),
	f(0,4),
	f(1,6)
	)
NegR  =Opcode(
	f(4,0),
	f(3,1)
	)
XorRR =Opcode(
	f(2,7),
	f(3,2)
	)	
SubRR =Opcode(
	f(5,0),
	f(4,1),
	f(3,3)
	)
SubRC =Opcode(
	f(5,1),
	f(4,2),
	f(3,4)
	)
JmpA  =Opcode(
	f(3,5)
	)
JmpiA =Opcode(
	f(3,6)
	)
IncR  =Opcode(
	f(4,3),
	f(3,7)
	)
DecR  =Opcode(
	f(4,4),
	f(6,0)
	)
ShrR  =Opcode(
	f(4,5),
	f(6,1)
	)
ShlR  =Opcode(
	f(4,6),
	f(6,2)
	)
JnzA  =Opcode(
	Pear("31 13 -5"),
	Pear("31 12 -5")
	)