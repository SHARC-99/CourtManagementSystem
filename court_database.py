import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="talloo05*",database="CMS")
cur = mydb.cursor()
#cur.execute("CREATE DATABASE CMS")
court = "CREATE TABLE court(CrimeNumber varchar(20),CrimeType varchar(20),StartDate varchar(20),LastDate varchar(20),JudgeName varchar(20),Person1Name varchar(20),Person2Name varchar(20),Person1Advocate varchar(20),Person2Advocate varchar(20),Person1phNo varchar(20),Person2phNo varchar(20),Person1Vitness varchar(20),Person2Vitness varchar(20),description varchar(500))"
cur.execute(court)