from common import *
from cpu_ref import *
import cpu_cmp_calc
from cpu_opcodes import f
import misc
print("SUP")
class CDU(Unit):
	def __init__(self,increaser,fetcher):
		self.increaser=increaser
		self.fetcher=fetcher
		
		misc.chatHub.breakRow()
		misc.chatHub.makeLink("--Fetch Next--",self.fetcher("/say One Fetch Cycle is Done."))
		misc.chatHub.breakRow()
	def getUnpackedPear(self, number):
		if number<0:
			raise Exception("negative is number is invalid")

		retPoint=Point(self.fetcher.register.dest.x,self.fetcher.register.dest.y+((number+1)*2),self.fetcher.register.dest.z)
		return Pear(retPoint,self.fetcher.register.size)
	def getCmdArg(self,order,size):
		return self.getUnpackedPear(order).getSubPear(size)
	def arg(self,order,size):
		return self.getCmdArg(order,size)
	def importNext(self):
		return self.increaser.pivot.get(self.fetcher.register)
	class Increaser:
		def __init__(self,iAdress,pivot):
			self.pivot=pivot
			self.iAdress=iAdress
	class Fetcher(LinkedComponent):
		def __init__(self,register,*args):
			LinkedComponent.__init__(self,args[0])
			self.register=register
			self.nodes=args
		def __getitem__(self,i):
			return self.nodes[i]

#CDU-command decoding unit
Cdu=CDU(
	CDU.Increaser(
		Pear("37 15 18",8),
		MatrixPivot("CDU_INCREASER",cpu_cmp_calc.Increaser.resRef.spawnPosition)
		),
	CDU.Fetcher(
		Pear("1 11 -5",8),
		f(5,4),
		f(5,5)
		)
	)

