import sqlite3
db = sqlite3.connect("gestion.db")  # on constate que le fichier est crée et il est vide
db.execute("create table if not exists person(code integer, name text)")
db.execute("delete from person where code=10")
db.execute("update person set name='Radi' where code = 12")
db.commit()
db.row_factory = sqlite3.Row
cursor = db.execute("select * from person")
for row in cursor :
    print(row["code"], row["name"])
db.close()