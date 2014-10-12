'''
from cpu_component import Component
from cpu_common import *

Screen_chars=list()
for x in xrange(0,94):
	y=str(104-x)
	Screen_chars.append("-199 "+y+" -162 -194 "+y+" -155")

Screen=Component(Pear(Point("-201 11 -184")), Pear(Point("-197 11 -182")))
Screen.inChar=Pear(Point("-201 11 -187"),8)
Screen.ioPivotX=Pear(Point("-201 11 -191"),8)
Screen.ioPivotY=Pear(Point("-201 11 -190"),8)
Screen.pivXIncrease=Component(Pear(Point("-201 11 -152")),Pear(Point("-196 11 -150")))
Screen.pivotStart=Point("-192 11 -192")
Screen.pivotName="SCREEN_PIVOT"
Screen.charPivotNameame="SCREEN_CHARPIVOT"
Screen.Morph=Group()
Screen.Morph.powerOff=Pear("-82 9 -42")
Screen.Morph.powerOn=Pear("-80 2 -34")
Screen.Morph.openArea=Area("-227 23 -189","-208 17 -167")
Screen.Morph.hiddenArea=Area("-227 16 -189","-208 11 -167")
Screen.Morph.anchor=Point("-80 10 -47")'''