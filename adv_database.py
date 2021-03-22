import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="talloo05*",database="CMSA")
cur=mydb.cursor()
court = "INSERT INTO ADV(AdvId,AdvName,DOB,phoneNo,Post,TenureStart,TenureEnd) VALUES(%s,%s,%s,%s,%s,%s,%s)"
info = [('1000','Archit Saxena','21 july 1956','456123789','IMCA','1970','2014'),('1001','Aparna','4 dec 1989','741852963','NHS Complaints','2009','-'),('1002','Arpit','8 nov 1967','753951486','IMHA','1980','-'),('1003','Shantanu P.Bisaria','15 apr 1947','9517536842','Care Act Advocate','1978','1999')]
cur.executemany(court,info)
mydb.commit()