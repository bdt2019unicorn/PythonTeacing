import sqlite3

connection = sqlite3.connect("hr.db")
connection.execute("INSERT INTO countries_copy(country_id, country_name, region_id) VALUES ('ZZ', 'defgh', 4) ")
connection.commit()
# cursor = connection.execute("select * from countries_copy"); 
connection.close()