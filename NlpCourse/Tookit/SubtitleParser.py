
#!/usr/bin/python3
 
import pymongo

# myclient = pymongo.MongoClient("mongodb://10.13.0.5:27017/")
# mydb = myclient["Media"]
# mycol = mydb["Subtitle"]




def ASSParser():
	paths = ['Better.Days.chs.ass'];
	for path in paths:
		file = open(path, 'r',encoding='utf-8')
		# for line in file.readlines():
		# 	print(line.strip())
		lines = file.readlines()

		# print(parts)
		for line in lines:
			if(len(line) == 0 or line.startswith("Dialogue:")==False):
				continue
			items=line.split(',')#分割字符串
			# print(len(items))

			startTime = items[1].strip()
			endTime = items[2].strip()
			text = items[9].strip().replace("{\\blur3}","")

			print(startTime)
			print(endTime)
			print(text)
			print()

			subtDic = {}
			subtDic['Type'] = 'Movie'
			subtDic['Name'] ='少年的你'##根据不同的字幕文件修改名称
			subtDic['Number'] = 1##根据不同的字幕文件修改序号
			subtDic['startTime'] = startTime
			subtDic['endTime'] = endTime
			subtDic['text'] = text
			
			# x = mycol.insert_one(subtDic)

def SRTParser():
	paths = ['4_Chinese.srt'];
	for path in paths:
		file = open(path, 'r',encoding='utf-8')
		# for line in file.readlines():
		# 	print(line.strip())
		content = file.read()
		parts = content.split('\n\n')
		# print(parts)
		for part in parts:
			if(len(part) == 0):
				continue
			items=part.split('\n')
			# print(len(items))
			timestr = items[1]
			timeArray = timestr.split('-->')
			startTime = timeArray[0].strip()
			endTime = timeArray[1].strip()
			text = items[2]

			subtDic = {}
			subtDic['Type'] = 'Movie'
			subtDic['Name'] ='中国爱情故事'##根据不同的字幕文件修改名称
			subtDic['Number'] = 1##根据不同的字幕文件修改序号
			subtDic['startTime'] = startTime
			subtDic['endTime'] = endTime
			subtDic['text'] = text
			
			# x = mycol.insert_one(subtDic)



# SRTParser()
ASSParser()




