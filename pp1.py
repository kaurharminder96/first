import mysql.connector
m=mysql.connector.connect(host="localhost",user="harminder kaur",password="harminder28192",database="pawan")
cursor=m.cursor()
#where
sql="SELECT * FROM emp1 WHERE address='abhowal'"
cursor.execute(sql)
myresult=cursor.fetchall()
for t in myresult:
 print(t)
#like
s="SELECT * FROM emp1 WHERE address LIKE'%l%'"
cursor.execute(s)
myresult=cursor.fetchall()
for i in myresult:
    print(i)
#orderby
q="SELECT * FROM emp1 ORDER BY name"
cursor.execute(q)
myresult=cursor.fetchall()
for r in myresult:
 print(r)
 #delete
 w = "DELETE FROM emp1 WHERE address='abhowal'"
 cursor.execute(w)
 m.commit()
 print(cursor.rowcount,"record(s)deleted")