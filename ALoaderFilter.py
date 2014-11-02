from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import json
import ntpath
from cpu_cmp_ram import tape

class ImageFile:
	def __init__(self,fileName):
		self.path=fileName
		self.slots=json.loads(open(self.path).read())
		print(len(self.slots))
	def save():
		with open(self.path, 'w',newline='') as outfile:
				json.dump(self.slots,outfile)
class Program:
	def __init__(self,fileNamew):
		self.path=fileName
		f=open(fileName,'r').read()
		self.adict=json.loads(f)
	def getBaseName(self):
		return ntpath.basename(self.path)
	def loadSegment(self,name,adress):
		print("choose"+name)
		toLoad=self.adict[name]
		stype=name[:5]
		toformat=name.split('.')[1]
		if stype==".code":
			for i , row in enumerate(toLoad):
				for block in row:
					if isinstance(block, str):
						try:
							block = block.format(**{toformat:adress})
						except KeyError:
							continue
				
				tape[start+i]=x
		
		elif stype==".data":
			#TODO
			raise Exception("loaiding data segments is unimplamented yet")
		tape.save()
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
		
		Label(self, text="to adress:").grid(row=2, column=1)
		self.adress=Entry(self)
		self.adress.grid(row=2,column=2)
		
		self.QUIT = Button(self, text="load", fg="blue",command=self.loadfile)
		self.QUIT.grid(row=3, column=2)

	def askFile(self):
		self.data =Program(askopenfilename(parent=root))
		self.opbutton["text"]=self.data.getBaseName()
		segments=self.data.getSegmentNames()
		self.m= OptionMenu(self,self.variable,*segments)
		self.m.grid(row=1, column=2,sticky=W+E)
	def loadfile(self):
		adress=self.adress.get()
		if adress[-1]=='h':
			adress=int(adress.split("h")[0],16)
		else:
			adress=int(adress)
		print(adress)
		self.data.loadSegment(self.variable.get(),adress)
		root.destroy()
tape=ImageFile("E:/a.json")	
root = Tk("Load Program")
app = Dialog(master=root)
app.mainloop()
