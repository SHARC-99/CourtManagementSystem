import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="talloo05*",database="CMSO")
cur=mydb.cursor()
court = "INSERT INTO PERSON(PersonId,PersonName,DOB,phoneNo,Post,TenureStart,TenureEnd) VALUES(%s,%s,%s,%s,%s,%s,%s)"
info = [('1010','R.VAISHNAVI','21 july 1956','456123789','Court Interpreter','1970','2014'),('1020','SIDTHARTH JINDAL','4 dec 1989','741852963','Corrections Officer','2009','-'),('1030','DEVANG MATHUR','8 nov 1967','753951486','Court Clerk','1980','-'),('1040','YOGITA DESHPANDEY','15 apr 1947','9517536842','Court Reporter','1978','1999')]
cur.executemany(court,info)
mydb.commit()