import sqlite3

connection = sqlite3.connect("hr.db") 

curror = connection.execute("SELECT * FROM countries") 
list = []
for row in curror: 
	print row
	list.append(row)

connection.close()