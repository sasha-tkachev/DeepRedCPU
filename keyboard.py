from common import *
import json
from cpu_ref import *


class Keyboard(Unit):
	#constructor
	def __init__(self,**args):
		self.mode="chat"
		self.window=args["window"]
		self.keymap=args["keymap"]
		self.onClick=args["onClick"]
		self.tmp=args["tempPear"]
		self.callListners=args["callListners"]
		self.pivot=args["pivot"]
		self.startlock=args["startlock"]
		self.stoplock=args["stoplock"]
		self.spec=args["spec"]
	
	#player interface selectors
	def checkh(self,i):
		intervals=[2,5,8,11,13]
		return self.checkLook(intervals[int(i)],intervals[int(i)+1], False,int(i))
	
	def checkw(self,i):
		intervals=[161, 163, 166, 169,172, 174,177 ,180,-177,-174,-172,-163,-168, -166,-164,-162,-160]
		return self.checkLook(intervals[int(i)],intervals[int(i)+1], True,int(i) )
	
	def checkLook(self,minRot,maxRot, isx, distance):
		if minRot==180:
			minRot=-180
		if minRot >maxRot:
			tmp =minRot
			minRot=maxRot
			maxRot=tmp
		toret="/execute @p["
		if isx:
			toret+="rym="+str(minRot)+",ry="+str(maxRot)
		else:
			toret+="rxm="+str(minRot)+",rx="+str(maxRot)
		
		toret+="] ~ ~ ~ /tp @e[name="+self.pivot.ID+"]"
		
		if isx:
			toret+=" ~"+str(distance)+" ~ ~"
		else:
			toret+=" ~ ~-"+str(distance+1)+" ~"
		return toret
	
	def key(self,c):
		if self.mode =="chat":
			return "/say "+str(c)
		elif self.mode =="screen":	
			return Literal.char(str(c)).clone(self.tmp)
	def openWindow(self):
		return "/fill "+self.window[0]+" "+self.window[1]+" barrier"
	
	def closeWindow(self):
		return "/fill "+self.window[0]+" "+self.window[1]+" quartz_block"
	
	def plant(self,s):
		r = self.callListners.dest + (0,-1,0)
		return "/setblock "+str(r)+" command_block 0 replace {Command:"+str(s)+"}"

_map=json.loads(open('E:/Games/Minecraft/mcedit/MCEdit-0.1.7.1.win-amd64/filters/data/keymap.json').read())

keyboard=Keyboard(
	keymap=_map,
	onClick=Pear("-76 7 -57"),
	pivot=CartPivot( "KEYBOARD_PIVOT", Point("-77 10 -52")),
	tempPear=Pear("-76 9 -58", 8),
	callListners=Pear("-68 7 -57"),
	window=["-71 12 -24","-70 12 -24"],
	startlock=Pear("-73 7 -23"),
	stoplock=Pear("-73 7 -22"),
	spec="-70.00001 11.38 -22",
)

