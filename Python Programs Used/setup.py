import os


print("lets start")
val=input("do you want to launch the software")


os.system("pip install tkintertable")
os.system("pip install PyMySQL")
os.system("pip install Pillow")
import  pymysql
con = pymysql.connect(host="localhost", user="root", password="1234")
cur = con.cursor()
cur.execute("CREATE DATABASE sms")
con.commit()

con1 = pymysql.connect(host="localhost", user="root", password="1234",database="sms")
cur1 = con1.cursor()
cur1.execute("CREATE TABLE course (name VARCHAR(45) NOT NULL,duration VARCHAR(45) NOT NULL,charges VARCHAR(45) NOT NULL,stream VARCHAR(45) NOT NULL,PRIMARY KEY (name))")
cur1.execute("CREATE TABLE student (roll INT NOT NULL,name VARCHAR(45) NOT NULL,email VARCHAR(45) NOT NULL,stream VARCHAR(45) NOT NULL,course VARCHAR(45) NOT NULL,gender VARCHAR(45) NOT NULL,contact VARCHAR(45) NOT NULL,dob VARCHAR(20) NOT NULL,address VARCHAR(45) NOT NULL,PRIMARY KEY (roll))")
cur1.execute("CREATE TABLE fees (roll INT NOT NULL,f1 VARCHAR(45) NOT NULL,f2 VARCHAR(45) NOT NULL,f3 VARCHAR(45) NOT NULL,f4 VARCHAR(45) NOT NULL,f5 VARCHAR(45) NOT NULL,f6 VARCHAR(45) NOT NULL,PRIMARY KEY (roll))")
cur1.execute("CREATE TABLE result (roll INT NOT NULL,sem1 VARCHAR(45) NOT NULL,sem2 VARCHAR(45) NOT NULL,sem3 VARCHAR(45) NOT NULL,sem4 VARCHAR(45) NOT NULL,sem5 VARCHAR(45) NOT NULL,sem6 VARCHAR(45) NOT NULL,PRIMARY KEY (roll))")
con1.commit()