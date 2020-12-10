import mysql.connector
import pandas
import xlsxwriter as xlsw

mydb = mysql.connector.connect(
  host="localhost",
  port= "3306",
  user="root",
  password="",
  database="may"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tenant")

myresult = mycursor.fetchall()
list = []
for x in myresult:
  print(x)
  list.append(x)


print(list)

df = pandas.DataFrame(list)
# df = df.transpose()
writer = pandas.ExcelWriter("connect-mysqlout.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name="Sheet1Name",startrow=1, startcol=1, header=False, index=False)
writer.save()