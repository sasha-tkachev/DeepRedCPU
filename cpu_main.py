from misc import Bunch
root=Bunch({
	"path":"E:/Games/Minecraft/mcedit/MCEdit-0.1.7.1.win-amd64/filters",
	"data":{
		"path":"E:/Games/Minecraft/mcedit/MCEdit-0.1.7.1.win-amd64/filters/data",
	}
})
#returns relative to root
def path(s):
	return root+"/"s