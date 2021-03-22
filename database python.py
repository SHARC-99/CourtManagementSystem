import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="talloo05*",database="db1")
cur =mydb.cursor()
################################################################################
#cur.execute("CREATE DATABASE db1")
#court ="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
#cur.execute(court)
###############################################################################
#enter="INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
#b1=[(2,"java",400),(3,"python2",500),(4,"python3",635),(5,"algorithm",578),(6,"probablity andqueing",448)]
#cur.executemany(enter,b1)
#mydb.commit()
###################################################################################
#show ="select * from book"
#cur.execute(show)
#result=cur.fetchall()
#for i in result:
#    print(i)
###################################################################################
#update="update book set price=price-100 where price>200"
#cur.execute(update)
#mydb.commit()
##################################################################################
delete ="delete from book where bookid='1000'"
cur.execute(delete)
mydb.commit()