from common import *

from cpu_ref import *
#old system
'''
sAL = "1 11 -8"
AL  = sAL + " 8 11 -8"
sAH = "9 11 -8"
AH  = sAH +" 16 11 -8"

sCL = "1 11 -10"
CL  = sCL+" 8 11 -10"
sCH = "9 11 -10"
CH  = sCH+" 16 11 -10"

sDL = "1 11 -12"
DL  = sDL+" 8 11 -12"
sDH = "9 11 -12"
DH  = sDH+" 16 11 -12"

sBL ="1 11 -14"
BL  =sBL+" 8 11 -14"
sBH = "9 11 -14"
BH  = sBH+" 16 11 -14"

#register setter
RegisterSetter = Component(Pear("-9 12 27"),Pear("-13 11 27"))
RegisterSetter.iId=Pear("-8 11 27",3)
RegisterSetter.iValue=Pear("-13 11 25",8)
RegisterSetter.pivot=CartPivot("REGISTER_SETTER_PIVOT",Point("-13 11 23"))
#register getter
RegisterGetter = Component(Pear("-9 12 35"),Pear("-13 11 35"))
RegisterGetter.iId=Pear("-8 11 35",3)
RegisterGetter.result=Pear("-13 11 33",8)
RegisterGetter.pivot=CartPivot("REGISTER_GETTER_PIVOT",Point("-13 11 31"))
'''


