
class Counter(object):
	worddic ={}
	
	def __init__(self):
		self.worddic ={}

	def add(self, word):
		if word in self.worddic:
			freq = self.worddic[word]
			freq = freq +1
			self.worddic[word]= freq
		else:
			self.worddic[word]= 1

	def addwordlist(self, wordlist):
		for word in wordlist:
			 self.add(word)
		return sorted()

	def sort(self):
		res = {k: v for k, v in sorted(self.worddic.items(), key=lambda item: item[1], reverse=True)}

		# for k, v in res.items():
		# 	print(k,v)
		return res

