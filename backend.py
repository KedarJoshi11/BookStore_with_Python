import sqlite3

def connect():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookshelf (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookshelf VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    #ID is an auto increment value, so we don't have to pass it manually. So, in its place we'll just put NULL
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookshelf")
    conn.commit()# This is redundant
    rows=cur.fetchall()
    conn.close()
    return rows

# We are going to implement an "OR" search. This means that the user will enter either a title, author, year or isbn number. Or the user may enter all of them at the same time.
def search(title="",author="",year="",isbn=""):
# we have passed some empty strings in the parameters. Because users might just enter the value of one parameter. So, passing empty default values will prevent errors.
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookshelf WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM bookshelf WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("UPDATE bookshelf SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("Demolition man", "Kedar Joshi", 2018, 1154384)
#delete(2)
#update(4,"The moon","John Smith", 1965, 4575587)
#print(view())
#print(search(author="John Smith"))
