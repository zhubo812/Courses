import mysql.connector
import os

def getMySQL():
	mydb = mysql.connector.connect(
  	host="192.168.1.107",
  	user="root",
  	passwd="admin",
  	database="media"
	)
	return mydb

def getFiles(dir):
    filelist=[]
    filenames = os.listdir(dir)
    for filename in filenames:
        filepath = dir+'/'+filename
        filelist.append(filepath)
    return filelist


def getSubtitle2DB():
	mydb = getMySQL()
	mycursor = mydb.cursor()

	files = getFiles('subtitle')

	for file in files:

		filename = file[file.index('/')+1:]
		print(filename)
		fileid = filename[:12]
		print(fileid)
		typename = filename[-3:]
		print(typename)
		f = open(file,'r',encoding='utf-8')
		lines = f.readlines()
		content = ''
		for line in lines:
			content= content+line.replace('\ufeff','')
		print(content)

		sql = "INSERT INTO subtitleIndex (id, type, content) VALUES (\"%s\", \"%s\", \"%s\")" % (fileid,typename,content)
			# sql = 'INSERT INTO paper (newsid) VALUES（11）'
			#paper为表名，newsid为插入数据的字段
		print(sql)
			
		mycursor.execute(sql)
			 
		mydb.commit()    # 数据表内容有更新，必须使用到该语句
	mydb.close()


if __name__ == '__main__':
	getSubtitle2DB()