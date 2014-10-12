from cpu_common import *
from cpu_component import *
from cpu_ref import *
class RAM_READ(Component):
	def __init__(self,peara,pearb,iAdress,oResult,pivot):
		Component.__init__(self,peara,pearb)
		self.iAdress=iAdress
		self.oResult=oResult
		self.pivot=pivot
class RAM_WRITE(Component):
	def __init__(self,peara,pearb,iAdress,iValue,pivot):
		Component.__init__(self,peara,pearb)
		self.iAdress=iAdress
		self.iValue=iValue
		self.pivot=pivot
#RAM
Ram=Unit()
Ram.Read=RAM_READ(
	Pear("28 14 23"),
	Pear("35 15 23"),
	Pear("28 11 23",8),
	Pear("1 11 1",8),
	CartPivot("RAM_READ_PIVOT",Point("28 11 25"))
	)
Ram.Write=RAM_WRITE(
	Pear("28 14 20"),
	Pear("35 15 20"),
	Pear("28 11 20",8),
	Pear("1 11 2",8),
	CartPivot("RAM_WRITE_PIVOT",Point("28 11 25"))
	)