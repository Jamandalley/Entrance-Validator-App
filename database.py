import mysql.connector as sql
mycon = sql.connect(host ='127.0.0.1', user ='root', passwd ='')
mycursor = mycon.cursor()
mycursor.execute("CREATE DATABASE sqi_db")
mycon = sql.connect(host ='127.0.0.1', user ='root', passwd ='', database = 'sqi_db')
mycursor = mycon.cursor()
mycursor.execute("CREATE TABLE customer_profile(matric_number VARCHAR(10) PRIMARY KEY, full_name VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, department VARCHAR(50) NOT NULL)")
mycursor.execute("ALTER TABLE customer_profile ADD password VARCHAR(50) NOT NULL")
mycon.commit()
