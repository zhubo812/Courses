

class ResourceUtil(object):
    def __init__(self):
        '''
        Constructor
        '''

	def loadStoplist(self):
		stoplist =[]
		file = open("stoplist.txt","r",encoding="utf-8")
		# stoplist = file.readlines()
		# for index in range(len(stoplist)):
		# 	stoplist[index] = stoplist[index].replace("\n","")
		for line in file:
			stoplist.append(line.replace("\n",""))

	def loadStoplist(self,path):
		stoplist =[]
		file = open(path,"r",encoding="utf-8")
		# stoplist = file.readlines()
		# for index in range(len(stoplist)):
		# 	stoplist[index] = stoplist[index].replace("\n","")
		for line in file:
			stoplist.append(line.replace("\n",""))