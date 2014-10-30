from common import *
import json
from cpu_ref import *
class RAM_READ(LinkedComponent):
	def __init__(self,peara,iAdress,oResult,pivot):
		LinkedComponent.__init__(self,peara)
		self.iAdress=iAdress
		self.oResult=oResult
		self.pivot=pivot
class RAM_WRITE(LinkedComponent):
	def __init__(self,peara,iAdress,iValue,pivot):
		LinkedComponent.__init__(self,peara)
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

class Tape:
	def __init__(self,isofile):
		#self.slots=[[None for _ in range(8)] for _ in range(256)]
			self.isofile=isofile
		if not isofile:
			
		else:
			self.slots=json.loads(open(self.image).read(isofile))
	def __getitem__(self,row):
		return self.slots[row]
	def __setitem__(self,row,value):
		self.slots[row]=value
	def save():
		open(options.inputFile).read()
tape=Tape()
