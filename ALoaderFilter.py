from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import json
import ntpath
from cpu_cmp_ram import tape
from Build_CPU import perform as build
class Program:
	def __init__(self,fileName):
		self.path=fileName
		f=open(fileName,'r').read()
		self.adict=json.loads(f)
	def getBaseName(self):
		return ntpath.basename(self.path)
	def loadSegment(self,name):
		toLoad=self.adict[name]
		stype=name[:5]
		if stype==".code":
			for i , x in enumerate(toLoad):
				for block in x:
					block = block.format(**{name:str(adress)})
				tape[start+i]=x
		
		elif stype==".data":
			#TODO
			raise Exception("loaiding data segments is unimplamented yet")
	def getSegmentNames(self):
		toRet=list()
		for key,value in self.adict.items():
			print(key)
			toRet.append(key)
		return toRet
class Dialog(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		self.data=""
		self.segment=""
	def createWidgets(self):
		Label(self, text="load from file:").grid(row=0, column=1)
		self.opbutton = Button(self)
		self.opbutton["text"]      = "open..."
		self.opbutton["command"] = self.askFile
		self.opbutton.grid(row=0, column=2,sticky=W+E)
		
		Label(self, text="segment:").grid(row=1, column=1)
		self.variable = StringVar(root)
		self.variable.set("segment") # default value
		self.m= OptionMenu(self,self.variable,"None")
		

		self.QUIT = Button(self, text="load", fg="blue",command=self.loadfile)
		self.QUIT.grid(row=2, column=2)

	def askFile(self):
		self.data =Program(askopenfilename(parent=root))
		self.opbutton["text"]=self.data.getBaseName()
		segments=self.data.getSegmentNames()
		self.m= OptionMenu(self,self.variable,*segments)
		self.m.grid(row=1, column=2,sticky=W+E)
	def loadfile(self):
		self.data.loadSegment(self.variable.get())
		root.destroy()
	
root = Tk("Load Program")
app = Dialog(master=root)

def perform(level, box, options):
	app.mainloop()
	build(level,box,options)
	pass
	