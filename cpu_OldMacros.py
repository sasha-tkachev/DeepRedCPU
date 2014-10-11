from cpu_common import *
from cpu_component import *
from cpu_ref import *
def CopyToCart(cartname, content):
	return "/execute @e[name="+cartname+"] ~ ~ ~ /clone "+content+" ~ ~ ~"
def SignalCart(cartname, block):
	return "/execute @e[name="+cartname+"] ~ ~ ~ /setblock ~ ~ ~ "+block
def SpawnCart(name, position):
	return "/summon MinecartRideable "+str(position)+" {CustomName:\""+name+"\"}"
def KillCart(name):
	return "/kill @e[name="+name+"]"
def Unlock(adress):
	UnlockBlock="sponge"
	return "/setblock "+adress+" "+UnlockBlock	
def TestSelect(selecor,calldest):
	return "/execute "+selecor+" ~ ~ ~ "+Call(calldest)

#CALLING
def Call(adress):
	if isinstance(adress, Component):
		return "/setblock "+str(adress.invokeEnter)+" redstone_block"
	return "/setblock "+str(adress)+" redstone_block"
def Invoke(component,exit,_power=0):
	def _getQmark(p):
		qm=None
		if(p>0):
			qm="\\"
		while(p>1):
			qm+=qm
			p-=1
		qm+="\""
		return qm
	toRet=None
	if isinstance(component,list):
		invokeList=component
		cur=invokeList.pop(0)
		if _power == 0:
			toRet+=\
				"/setblock "+str(cur.invokeEnter)+" command_block 0 replace { Command:\""+\
				"/setblock "+str(cur.invokeExitBlock)+" command_block 0 replace "+\
				Invoke(invokeList,exit,_power+1)+"}"
			
			if(len(invokeList)==0):
				toRet+="{Command:\\\"/setblock "+str(exit)+" redstone_block\\\"}\"}"
		return "{"+_getQmark(_power)+"/setblock "+str(cur.invokeEnter)+" command_block 0 replace {Command:"+_getQmark(_power+1)+"/setblock "+str(cur.invokeExitBlock)+" command_block 0 replace "+Invoke(invokeList,exit,(_power+2))
	
	return "/setblock "+str(component.invokeEnter)+" command_block 0 replace {Command:\"/setblock "+str(component.invokeExitBlock)+" command_block 0 replace {Command:\\\"/setblock "+str(exit)+" redstone_block\\\"}\"}"
	


def SpawnFrame(x,y,z,char="0"):
		fx=-77
		fy=11
		fz=-42
		fx+=x
		fy-=y
		fz+=z
		fx=str(fx)
		fy=str(fy)
		fz=str(fz)
		return "/summon ItemFrame "+fx+" "+fy+" "+fz+" {TileX:"+fx+",TileY:"+fy+",TileZ:"+fz+",Facing:0,Item:{id:358,Damage:"+str(ord(char))+",Count:1}}"