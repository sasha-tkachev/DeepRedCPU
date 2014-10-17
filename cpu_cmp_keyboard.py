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
	def CheckLookWidth(self,i):
		intervals=[161, 164, 167, 169,172,175,177 ,-180,-177,-174,-171,-169,-166, -163,-158]
		return Keyboard_CheckLook(intervals[int(i)],intervals[int(i)+1], True,int(i) )
	def CheckLook(self,minRot,maxRot, isx, distance):
		toret="/execute @p["
		if isx:
			toret=toret+"ry="+str(maxRot)+",rym="+str(minRot)
		else:
			toret=toret+"rx="+str(maxRot)+",rxm="+str(minRot)
		
		toret=toret+"] ~ ~ ~ /tp @e[name="+Keyboard_pivot+"] ~ ~ ~-"

		toret=toret+str(distance)

		return toret
	def Key(self,c):
		
		return Clone(Literals.Char(c),self.tmp)

keyboard=Keyboard(
	"leaves",
	["-15 13 -21", "-16 13 -21"],
	"-17 11 -53",
	CartPivot( "KEYBOARD_PIVOT", Point("-22 15 -46")),
	Pear("1 11 -54", 8)
)
 	
