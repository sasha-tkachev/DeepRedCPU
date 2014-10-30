import tkinter as tk
from tkinter.filedialog import *
from tkinter.simpledialog import *
class SegmentSelector(Dialog):

	def body(self, master):

		Label(master, text="segment:").grid(row=0)
		self.e1 = Entry(master)
		self.e1.grid(row=0, column=1)
		return self.e1 # initial focus
	def apply(self):
		self.result = self.e1.get()

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		self.data=""
		self.segment=""
	def createWidgets(self):

		self.hi_there = tk.Button(self)
		self.hi_there["text"]      = "select a file"
		self.hi_there["command"] = self.askFile
		self.selectSegment = tk.Button(self)
		self.selectSegment["text"] = "select a segment"
		self.selectSegment["command"] = self.askSegment
		self.hi_there.pack(side="top")
		self.selectSegment.pack(side="top")
		self.QUIT = tk.Button(self, text="load", fg="blue",
											command=self.loadfile)
		self.QUIT.pack(side="bottom")

	def askFile(self):
		self.data = askopenfilename(parent=root)

	def loadfile(self):
		print("loading segment {seg} from file{data}".format(seg=self.segment,data=self.data))
		root.destroy()
	def askSegment(self):
		s= SegmentSelector(root)
		self.segment=s.result
root = tk.Tk()
app = Application(master=root)
app.mainloop()

def perform(level, box, options):
	pass
	