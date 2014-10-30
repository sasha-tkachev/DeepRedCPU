import json
from cpu_cmp_ram import tape

def load(fileName,segmentname,adress):
	f=open(fileName,'r').read()
	adict=json.loads(f)
	toLoad=adict[segmentname]
	stype=segmentname[:5]
	if stype==".code":
		for i , x in enumerate(toLoad):
			for block in x:
				block = block.format(**{segmentname:str(adress)})
			tape[start+i]=x
	
	elif stype==".data":
		#TODO
		raise Exception("loaiding data segments is unimplamented yet")
		


