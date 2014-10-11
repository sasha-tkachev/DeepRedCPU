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
