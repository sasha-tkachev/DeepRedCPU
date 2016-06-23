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
	def __init__(self,isofile,**args):
		#
		self.corner=args["corner"]
		self.isofile=isofile
		self.raw=json.loads(open(self.isofile).read())
		self.slots=self.raw['slots']
		self.vars=self.raw['vars']
	def __getitem__(self,row):
		return self.slots[row]
	def __setitem__(self,row,value):
		self.slots[row]=value
	def save():
		with open(self.isofile, 'w',newline='') as outfile:
			json.dump(self.slots,outfile)
	def reset():
		self.slots=[[None for _ in range(8)] for _ in range(256)]
		self.save()
tape=Tape("E:/cs/proj/DeepRedAssembler/bin/img.json",
	corner=Point(28,11,25)
	)
