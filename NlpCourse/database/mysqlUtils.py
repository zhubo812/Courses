import mysql.connector
 
mydb = mysql.connector.connect(
  host="192.168.1.107",
  user="root",
  passwd="admin",
  database="media"
)

# print(mydb)
mycursor = mydb.cursor()
 
# mycursor.execute("SHOW DATABASES")
 
# for x in mycursor:
#   print(x)

sql = "SELECT text FROM subtitle LIMIT 200"

mycursor.execute(sql)
 
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
 
for x in myresult:
  print(x)