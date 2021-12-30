import os

#文件内容为分好词且无词性标记
# wordlist = open('text.txt', 'r',encoding='utf-8').read().split()

# print(wordlist)

#文件内容为分好词且无词性标记
# wordlist=[]
# file = open('text.txt', 'r',encoding='utf-8')
# for line in file:
# 	# print(line)
# 	for word in line.split():
# 		wordlist.append(word)
# print(wordlist)

def getFiles(direc):#首先要获取到指定文件夹(dir)内所有文本的路径
	filelist=[]
	filenames = os.listdir(direc)#相对路径
	for filename in filenames:
		filepath = direc+'/' + filename
		filelist.append(filepath)
	return filelist


def getAllFiles(file_path):
    os.chdir(file_path)
    # print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(getAllFiles(file_path+'\\'+f))
            os.chdir(file_path)
        else:
            files.append(file_path+'\\'+f)
    return files

wordlist=[]
worddic = {}
filelist = getAllFiles('E:/temp/2/sogoulex')
print(filelist)

# for filePath in filelist:
# 	singlewordlist = open(filePath, 'r',encoding='utf-8').read().split()
# 	for word in singlewordlist:
# 		wordlist.append(word)
# for filePath in filelist:
# 	file = open(filePath,'r',encoding='utf-8')
# 	for line in file:
# 		for word in line.split():
# 			# wordlist.append(word)
# 			if word in worddic:
# 				worddic[word]= worddic[word]+1
# 			else:
# 				worddic[word]=1

# print(worddic)

# print(len(worddic))