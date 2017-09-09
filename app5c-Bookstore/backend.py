import sqlite3

def connect():
	  conn = sqlite3.connect("books.db")
	  cur = conn.cursor()
	  cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
	  conn.commit()
	  conn.close()



def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,isbn)) 
    #need to pass the NULL value to allow SQL to automatically insert and auto-inrement the ID

    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows




def search(title="", author="", year="", isbn=""):
	#note the variables passed are "initialised to empty"
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
	rows = cur.fetchall()
	conn.close()
	return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update (id, title, author, year, isbn):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
	conn.commit()
	conn.close()




connect()
#insert("Topolino","bomba",1985,12345336)
#delete(7)
#update(5,"nuovo titolo","nuovo autore",1999,999)
#update(2,"new title","gian",1987,9999)
#print(view())
#print(search(author="gian"))


