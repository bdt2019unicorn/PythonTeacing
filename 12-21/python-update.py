import sqlite3

connection = sqlite3.connect("hr.db")
connection.execute("UPDATE countries_copy SET country_name = '123456' WHERE country_id = 'ZZ'")
connection.commit()
connection.close()