import sqlite3
db = sqlite3.connect("gestion.db")  # on constate que le fichier est crée et il est vide
db.execute("delete from person")
db.execute("create table if not exists person(code integer, name text)")
db.execute("insert into person(code,name) values(?,?)", (10, "Karim"))
db.execute("insert into person(code,name) values(?,?)", (11, "Amal"))
db.execute("insert into person(code,name) values(?,?)", (12, "Reda"))
db.commit()
db.row_factory = sqlite3.Row
cursor = db.execute("select * from person")
for row in cursor :
    print(row["code"], row["name"])
db.close()
