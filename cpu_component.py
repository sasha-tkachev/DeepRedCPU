from cpu_common import *
from cpu_component import *
from cpu_ref import *
class Component:
	def __init__(self, invokeEnter, invokeExitBlock):
		#pear with the isze of 1
		self.invokeEnter=invokeEnter
		#point
		self.invokeExitBlock= invokeExitBlock
	def invoke(self,exit):
		return "/setblock "+str(self.invokeEnter)+" command_block 0 replace {Command:\"/setblock "+str(self.invokeExitBlock)+" command_block 0 replace {Command:\\\"/setblock "+str(exit)+" redstone_block\\\"}\"}" 
	def __call__(self,exit):
		return self.invoke(exit)
class Component1(Component):
	def __init__(self, invokeEnter, invokeExitBlock,iNumberA,oResult,_proa,_proc):
		Component.__init__(self,invokeEnter,invokeExitBlock)
		self.iNumberA=iNumberA
		self.oResult=oResult
		self._proa=_proa
		self._proc=_proc
		self.iValue=_proa
class Component2(Component1):
	def __init__(self, invokeEnter, invokeExitBlock,iNumberA,iNumberB,oResult,_proa,_prob,_proc ):
		Component1.__init__(self, invokeEnter, invokeExitBlock,iNumberA,oResult,_proa,_proc)
		self.iNumberB=iNumberB
		self._prob=_prob