import sqlite3
db = sqlite3.connect("gestion.db")
db.execute("create table if not exists person(code integer, name text)")

def afficher(code, name):
    cursor = db.execute("select * from person")
    for row in cursor :
        print(row["code"], row["name"])
        db.commit()

def inserer(code, name):
    db.execute("insert into person(code,name) values(?,?)", (code, name))
    db.commit()

def update(code, name):
    db.execute(f"update person set name = {name} where code = {code} " )
    db.commit()

def delete(code):
    db.execute(f"delete from person where code= {code}")
    db.commit()


print(afficher())
