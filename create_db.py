import sqlite3
def create_db():
  con=sqlite3.connect(database=r'ims.db')
  cur=con.cursor()
  
  #====Create Employee Table===
  
  cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,nid text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
  con.commit()
  
  #====Create Supplier Table===
  
  cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
  con.commit()
  
  #====Create Category Table===
  
  cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
  con.commit()
  
  #====Create Product Table===
  
  cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price text,quantity text,status text)")
  con.commit()
  
create_db()