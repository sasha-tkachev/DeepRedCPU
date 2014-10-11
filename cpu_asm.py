from cpu_common import *
from cpu_component import Component
class Row:
class SubrutineAssembler:
	def assemble(self,subs):
		self.frameCount=[0,0,0,0,0]	
		for sub in subs :
			self.allocSub(sub)
	def allocSub(self,sub):
		frames=[]
		tmp=[]
		i=0
		for cmd is sub.cmds:
			tmp.append(cmd)
			if isinstance(cmd[0],Component.invoke) or i >4:
				f=frame(tmp)
				frames.append(f)
				tmp=[]
				i=0
			i+=1
	def frame(self,cmd):
		#construct frame 
		f = _Frame(cmd):
		#set frame id 
		power = f.getPower()
		f.id = (frameCount[power-1],power)
		frameCount[power-1]+=1
		return f
	def bindToCords(self,blockStarts):
		
class _Frame:
	def __init__(self,cmds,ID):
		if isinstance(cmds,list):
			raise Exception("cmd must be a list")
		if len(cmds) > 4 :
			raise Exception("cmd length cannot be more then 4")
		self.cmds=cmds
		last=cmds[len(cmds)-1]
		self.powerblock=None
		if isinstance(last,Component.__call__):
			self.invoker = cmds[last]
			cmds.append((_Frame.reset,last+1))
		elif isinstance(last,Pear.__call__):
			self.carry=last
	def bindTo(self,frame):
		self.nextFrame=frame
	def bindInvoker(self):
		self.invoker[2] = self.nextFrame.getEnter()
	def binfCarry(self,i):
		self.carry[1]=self.nextFrame.getEnter()
	def getPower(self):

		return len(self.cmd)
	def getEnter(self):
		pass
	def reset(self,side):
		s=None
		if side = 3
			s= "~ ~ ~1"
		if side = 2:
			s= "~ ~ ~-1"
		if side = 0:
			s= "~ ~1 ~"
		if side = 1:
			s= "~ ~-1 ~"
		return "/setblock {} {}".format(s,Pear.resetBlock)
class Subrutine:
	def __init__(self,cmds,exit):
		'''	cmd is a list of touples that holding a function and a parameter
			exit is the callback destenation of the sub'''
		if not isinstance(exit,Pear):
			if isinstance(exit,str) or isinstance(exit,Point):
				exit = Pear(exit)
			else
				raise Exception("exit have  to be a pear or a string representing a point")
		self.cmds=cmds
		self.enterPear=None
		self.exit=exit
