import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="talloo05*",database="CMSJ")
cur=mydb.cursor()
court = "INSERT INTO JUDGE(judgeId,judgeName,DOB,phoneNo,Post,TenureStart,TenureEnd) VALUES(%s,%s,%s,%s,%s,%s,%s)"
info = [('0001','Shwetabh Saxena','21 july 1956','456123789','Chief Justice','1970','2014'),('0002','Paritosh','4 dec 1989','741852963','Justice H.C.','2009','-'),('0003','R.K.Saxena','8 nov 1967','753951486','Chief Justice H.C.','1980','-'),('0004','S.K.Bisaria','15 apr 1947','9517536842','Chief Justice','1978','1999')]
cur.executemany(court,info)
mydb.commit()