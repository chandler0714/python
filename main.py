import sqlite3

#def save:
print("create a database")
id = input("id: ")
#name = input("name: ")
#age = input("age: ")
con = sqlite3.connect('schoolbook.db')
cur = con.cursor()
#cur.execute('CREATE TABLE studnets(id integer primary key)')
cur.execute("insert into studnets(id) Values('{}')".format(id))
con.commit()
con.close()