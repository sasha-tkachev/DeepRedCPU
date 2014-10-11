#search for command blocks, eval what is between the ^^
from pymclevel 			import TAG_List
from pymclevel 			import TAG_Byte
from pymclevel 			import TAG_Int
from pymclevel 			import TAG_Compound
from pymclevel 			import TAG_Short
from pymclevel 			import TAG_Double
from pymclevel 			import TAG_String
from cpu_common 		import *
from cpu_component 		import *
from cpu_registers 		import *
from cpu_cmp_logic		import *
from cpu_cmp_calc		import *
from cpu_cmp_cdu 		import *
from cpu_cmp_keyboard	import *
from cpu_cmp_ram 		import *
from cpu_ref 			import *

displayName = "Build CPU"

def perform(level, box, options):
	s= M()
	print(s.x)
	Literals=Literal()
	#Old functions
	UnlockBlock="sponge"
	#ElseStackRegister=Pear(sBL,8)
	#RAM
	Ram=Unit()
	Ram.Read=RAM_READ(
		Pear("28 14 23"),
		Pear("35 15 23"),
		Pear("28 11 23",8),
		Pear("1 11 1",8),
		CartPivot("RAM_READ_PIVOT",Point("28 11 25"))
		)
	Ram.Write=RAM_WRITE(
		Pear("28 14 20"),
		Pear("35 15 20"),
		Pear("28 11 20",8),
		Pear("1 11 2",8),
		CartPivot("RAM_WRITE_PIVOT",Point("28 11 25"))
		)
	#ALU
	
	
	Adder=ADDER(
		Pear(Point("37 14 9")),#invoke enter
		Pear(Point("44 14 6")),#invoke exit
		Pear("1 11 6",8),#inumba
		Pear("1 11 7",8),#inumberb
		Pear("1 11 8",8),#oResultt
		Pear("37 14 12",8),#_proa
		Pear("37 14 11",8),#_prob
		Pear("37 14 10",8),#_proc
		Point("37 12 16"),#carts
		CartPivot("ADDER_CALLER",Point("37 11 8")),#caller
		Pear("37 13 7"),#stage2c
		Pear("37 11 11"),#stage3
		Pear("37 13 6"),#stage4
	)
	
	def ClearAdder():		
		return "/fill 57 12 16 64 12 17 stone"
		
	ALU_invert_io="57 16 10 "
	

	#flags
	
	
	#Screen
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
	Screen.Morph.anchor=Point("-80 10 -47")
	#Keyboard
	keyboard=Keyboard(
		"leaves",
		["-15 13 -21", "-16 13 -21"],
		"-17 11 -53",
		CartPivot( "KEYBOARD_PIVOT", Point("-22 15 -46")),
		Pear("1 11 -54", 8)
	)
 	#CDU-command decoding unit
 	Cdu=CDU(Pear("1 11 -5",8))
 	#commands adresses
 	Commands=Group()
 	Commands.Mov=Group()
	Commands.Mov.RR=Component(
		Pear("-7 15 11"),
		Pear("-7 15 18")
		)
	Commands.Mov.RM=Component(
		Pear("-5 15 11"),
		Pear("-5 15 18")
		)
	Commands.Mov.MR=Component(
		Pear("-7 18 11"),
		Pear("-7 17 18")
		)
	Commands.Mov.RC=Component(
		Pear("-5 18 11"),
		Pear("-5 17 15")
		)
	Commands.Mov.MC=Component(
		Pear("-5 19 17"),
		Pear("-5 19 13")
		)

	Commands.Sub=Group()
	Commands.Sub.RC=Component(
		Pear("-17 18 10"),
		Pear("-17 17 17")
		)
	
	Shifter=SHIFTER(
		Pear("16 14 14"),
		Pear("19 14 14"),
		Pear("1 11 11",8),
		Pear("1 11 10",8),
		Pear("14 11 14",8),
		False
		)
	DeShifter=SHIFTER(
		Pear("16 14 12"),
		Pear("19 14 12"),
		Pear("1 11 13",8),
		Pear("1 11 12",8),
		Pear("14 11 12",8),
		True
		)
	
	Increaser=INCREASER(
		Pear("40 15 23"),
		Pear("43 14 23"),
		Pear("1 11 15",8),
		Pear("1 11 16",8),
		Pear("37 11 23",8),
		CartPivot(
			"INCREASER_PIVOT",
			Point("37 11 27"),
			),
		)
	Decreaser=INCREASER(
		Pear("40 15 21"),
		Pear("43 14 21"),
		Pear("1 11 17",8),
		Pear("1 11 18",8),
		Pear("37 11 21",8),
		CartPivot(
			"DECREASER_PIVOT",
			Point("37 11 25")
			),
		)
	
	Inverter=INVERTER(
		Pear("38 15 19"),
		Pear("41 14 19"),
		Pear("1 11 19",8),
		Pear("1 11 20",8),
		Pear("37 11 19",8),
		)
	
	Orer=ORER(
		Pear("44 14 19"),Pear("44 14 14"),#invokes
		Pear("1 11 21",8),Pear("1 11 22",8),Pear("1 11 23",8),#interface
		Pear("37 15 15",8),Pear("37 14 16",8),Pear("37 15 16",8),#internalMem
		Pear("37 15 14"),Pear("37 21 18")#internalPointers
	)
	Xorer=XORER(
		Pear("43 18 18"),Pear("42 17 18"),#invokes
		Pear("1 11 24",8),Pear("1 11 25",8),Pear("1 11 26",8),#interfaces
		Pear("37 17 20",8),Pear("37 19 20",8),Pear("37 18 20",8),#internalSlots
		Area("44 17 19","44 19 19"),Area("43 17 19","43 19 19"),#banks
		Pear("37 18 23"),#_test
		Pear("38 14 3"),#testrecall
		)
	Fetch=FETCH(
		Pear("10 12 -5"),Pear("10 -1 -1"),#invokes
			(
				Pear("11 14 -5"),
				Pear("11 15 -5"),
			),#hooks
		Pear("1 11 -5",8),#decodeRegister
		)
	
	for (chunk, slices, point) in level.getChunkSlices(box):
		for t in chunk.TileEntities:
			_x = t["x"].value
			_y = t["y"].value
			_z = t["z"].value
			
			if _x >= box.minx and _x < box.maxx and _y >= box.miny and _y < box.maxy and _z >= box.minz and _z < box.maxz and t["id"].value == "Control":
				command = t["Command"].value
				command=command.replace("/say `","`")
				
				Print("[parsing] "+command)
				i = 0
				till=len(command)

				toeval=""
				result=""

				flag=True
				alert='`'
				while i<till:
					char =command[i]
					if flag:
						if char==alert:
							flag=False
						else:
							result+=char
					else:
						if char==alert:
							flag=True
							result+=str(eval(toeval))
							toeval=""
						else:
							toeval+=char
					i=i+1

					
				t["Command"] = TAG_String(result)
				
				chunk.dirty = True
