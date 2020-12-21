import sqlite3

connection = sqlite3.connect("hr.db")
# cursor = connection.execute("INSERT INTO countries(country_id, country_name, region_id) VALUES ('DE', 'defgh', 4) ")
cursor = connection.execute("select * from countries_copy"); 
connection.close()