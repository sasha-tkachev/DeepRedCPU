from common import *

from cpu_ref import *
class Keyboard(Unit):
	#constructor
	def __init__(self,clickBlock,clickArea,onClick,pivot,tmpPear):
		self.clickBlock=clickBlock
		self.clickArea=clickArea
		self.userClick=onClick
		self.pivot=pivot
		self.tmp=tmpPear
	#player interface selectors
	def checkh(self,i):
		intervals=[2,5,8,11,13]
		return self.checkLook(intervals[int(i)],intervals[int(i)+1], False,int(i))
	def checkw(self,i):
		intervals=[161, 164, 167, 169,172,175,177 ,-180,-177,-174,-171,-169,-166, -163,-158]
		return self.checkLook(intervals[int(i)],intervals[int(i)+1], True,int(i) )
	def checkLook(self,minRot,maxRot, isx, distance):
		toret="/execute @p["
		if isx:
			toret+="ry="+str(maxRot)+",rym="+str(minRot)
		else:
			toret+="rx="+str(maxRot)+",rxm="+str(minRot)
		
		toret=toret+"] ~ ~ ~ /tp @e[name="+self.pivot+"]"
		
		if isx:
			toret+=" ~-"+str(distance)+" ~ ~"
		else:
			toret+=" ~ ~-"+str(distance)+" ~"
		return toret
	def Key(self,c):	
		return Clone(Literals.Char(c),self.tmp)

keyboard=Keyboard(
	"leaves",
	["-15 13 -21", "-16 13 -21"],
	"-76 7 -57",
	CartPivot( "KEYBOARD_PIVOT", Point("-77 9 -52")),
	Pear("-76 9 -58", 8)
)

