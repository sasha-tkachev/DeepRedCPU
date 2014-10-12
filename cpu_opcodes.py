
from cpu_common import *
class Opcode(Component):
	def __init__(self,invokeEnter,subStart,l=None):
		Component.__init__(self,invokeEnter)
		self.subStart=subStart
		self.subReturn=Point(invokeEnter.x+1,invokeEnter.y,invokeEnter.z)
		self.l=l
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

MovRC=Opcode(
	Point("34 26 23"),
	Pear("28 12 17")
	)
