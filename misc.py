import common
class Bunch(object):
  def __init__(self, adict):
    self.__dict__.update(adict)
#lets you put messages that do stuff
class ChatHub():
	maxRow=5
	def __init__(self,name,start):
		self.links=[]
		self.start=start
		self.name=name
		self.rowStreak=0
	def makeLink(self,name,command):
		if self.rowStreak > ChatHub.maxRow:
			self.rowStreak=0
			name+="\n"
		self.links.append((name,command))
	def breakRow(self):
		self.rowStreak=0
	def show(self):
		start=self.start
		toRet='/tellraw @p { "text":"==='+self.name+'===]\\n","extra":['
		i=0
		for link in self.links:
			cmd="/setblock {} {} {} redstone_block".format(start.x,start.y,start.z+i)
			toRet+='{"text":"'+link[0]+' ","clickEvent":{"action":"run_command","value":"'+cmd+'"}}'
			i+=1
			if i <len(self.links):
				toRet+=","
			

		toRet+=']}'
		print ("saying to the chat "+toRet)
		return toRet
	def action(self,i):
		try:
			return self.links[i][1]
		except IndexError:
			return "/say This link is broken"
chatHub=ChatHub("LinkHub",common.Point(46,12,-3))