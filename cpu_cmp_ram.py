from common import *

from cpu_ref import *
class RAM_READ(Component):
	def __init__(self,peara,iAdress,oResult,pivot):
		Component.__init__(self,peara)
		self.iAdress=iAdress
		self.oResult=oResult
		self.pivot=pivot
class RAM_WRITE(Component):
	def __init__(self,peara,iAdress,iValue,pivot):
		Component.__init__(self,peara)
		self.iAdress=iAdress
		self.iValue=iValue
		self.pivot=pivot
#RAM
Ram=Unit()
Ram.Read=RAM_READ(
	Pear("37 14 20"),
	Pear("37 11 20",8),
	pPool.safeAlloc(),
	CartPivot("RAM_READ_PIVOT",Point("28 11 25"))
	)
Ram.Write=RAM_WRITE(
	Pear("37 14 19"),
	Pear("37 11 19",8),
	pPool.safeAlloc(),
	CartPivot("RAM_WRITE_PIVOT",Point("28 11 25"))
	)