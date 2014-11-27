from common import *
from cpu_ref import *
import cpu_cmp_calc
from cpu_opcodes import f
import misc
import cpu_registers

class CDU(Unit):
	def __init__(self,increaser,fetcher,interpreter):
		self.increaser=increaser
		self.fetcher=fetcher
		self.interpreter=interpreter
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
		return self.increaser.pivot.get(cpu_registers.ipRegister)
	def reset(self):
		return self.fetcher.register.setFalse()
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
	class Interpreter:
		def __init__(self,pivot,args):
			self.pivot=pivot
			self.actions=args
		def action(self,i,toMove):
			if toMove:
				return self.pivot.moveX(i+1)
			if i == 0 :
				return self.pivot.signal()
			return self.pivot.execute("/fill ~ ~ ~ ~-{} ~ ~ redstone_block".format(i))
		def interprate(self,numOfBits):
			return self.actions[numOfBits]()
		def __getitem__(self,i):
			return self.actions[i-1]
		def reset(self):
			p = self.pivot.spawnPosition
			new = Point(p.x+1,p.y,p.z)
			return "/fill {} {}".format(Pear(new,7).getOrigin(),Pear.resetBlock)
	
#CDU-command decoding unit
def s(start, i):
	p=[]
	for x in range(i):
 		p.append(Pear(Point(start.x+x,start.y,start.z)))
	return p
Cdu=CDU(
	CDU.Increaser(
		Pear("37 15 18",8),
		MatrixPivot("CDU_INCREASER",cpu_cmp_calc.Increaser.resRef.spawnPosition)
		),
	CDU.Fetcher(
		Pear("1 11 -5",8),
		f(5,4),
		f(5,5)
		),
	CDU.Interpreter(
		pRefrence("INTERPRETER",Point(1,10,-5)),
		s(f(7,0).dest,8)
	)
)