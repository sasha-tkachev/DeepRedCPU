class Screen(LinkedComponent):
	def __init__(self,**f):
		self.frames=f['frames']
		LinkedComponent.__init__(self,self.frames[0])
		self.iCursor=f["iCursor"]
		self.cursor=f["cursor"]
		self.tmpcursor=f['tmpcursor']
		self.iChar=f['iChar']
		self.charpivot=f['charpivot']
		self.snapStart=f['snapStart']
		
	def clearAction(self):
		return "/fill {} {} {}".format(self.tmpcursor.dest,self.iChar.getEndOfOrigin(),Pear.resetBlock)
	def char(self,i):
		a=Point(self.snapStart[0][0],self.snapStart[0][1]+i,self.snapStart[0][2])
		b=Point(self.snapStart[1][0],self.snapStart[1][1]+i,self.snapStart[1][2])
		return self.cursor.execute("/clone {} {} ~ ~ ~".format(a,b))
	def __getitem__(self,i):
		return self.frames[i]
screen=Screen(
	snapstart=((-199,0,-162)(-194,0,-155)),
	frames=[
		Point("-202 12 -189"),
		Point("-201 12 -189"),
		Point("-198 12 -189")
	],
	tmpcursor=Pear("-202 11 -192",8),
	iChar=Pear("-202 11 -191",8),
	charpivot=pRefrence("SCREEN_CHARPIVOT",Point("-194 12 -180")),
	cursor=pRefrence("CURSOR",Point("-192 11 -192"))
	)