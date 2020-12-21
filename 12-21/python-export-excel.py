import pandas
import xlsxwriter as xlsw
import sqlite3

connection = sqlite3.connect("hr.db") 

curror = connection.execute("SELECT * FROM countries") 
list = []
for row in curror: 
	list.append(row)

connection.close()

df = pandas.DataFrame(list)
writer = pandas.ExcelWriter("countries-list.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name="CountriesList",startrow=0, startcol=0, header=False, index=False)
writer.save()