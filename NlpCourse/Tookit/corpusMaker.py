import mysql.connector
import jieba
import jieba.posseg as pseg

def getMySQL():
	mydb = mysql.connector.connect(
  	host="192.168.1.107",
  	user="root",
  	passwd="admin",
  	database="paper"
	)
	return mydb


def getDataFromDB():
	files = []
	mydb = getMySQL()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM paper")
	myresult = mycursor.fetchall()     # fetchall() 获取所有记录
	for x in myresult:
		# print(x[2])
		files.append(x[2])
	return files

def getSentences(line):
	sentences =[]
	sentenceSpliter=["。","？","?","！","!","……","\n"]
	# print(line)
	start=0

	for index in range(len(line)):
		char = line[index]
		if(char in sentenceSpliter):
			sen = line[start:index+1]
			sentences.append(sen)
			start = index+1
		if(index == len(line)-1 and start < index):
			sen = line[start:]
			sentences.append(sen)
	return sentences

def getNGrams(wordlist, n):
    return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

def kwicCounter(ngrams):
	kwicdict = {}
	for n in ngrams:
		if n[2] not in kwicdict:
			kwicdict[n[2]] = [n]
		else:
			kwicdict[n[2]].append(n)

	# print(kwicdict )
	return kwicdict

def searchWord(kwicdict, keyword):
	if keyword in kwicdict:
		for val in kwicdict[keyword]:
			# print(type(val))
			# print(val)
			# print(val[:2])
			outstring = ' '.join(val[:2]).rjust(20)
			outstring += ' '
			outstring += ' '.join(str(val[2]).center(len(val[2])+6))
			outstring +=' '
			outstring += ' '.join(val[3:])
			print(outstring)
	else:
		print('There\'s no keyword')

if __name__ == '__main__':
	files = getDataFromDB()
	for file in files:
		sentences = getSentences(file)
		for sen in sentences:
			if(len(sen.strip()) == 0):
				continue
			print(sen)
			words = jieba.cut(sen.strip(),cut_all=False)
			# print(type(words))
			wlist = []
			for word in words:
				wlist.append(word)
			ngram = getNGrams(wlist,5)
			# print(ngram)
			kwic = kwicCounter(ngram)
			print(kwic)

			searchWord(kwic, '中')
			break
		break