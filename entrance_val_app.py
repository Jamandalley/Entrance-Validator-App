import mysql.connector as sql
# mycon = sql.connect(host ='127.0.0.1', user ='root', passwd ='')
# mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE sqi_db")
# mycon = sql.connect(host ='127.0.0.1', user ='root', passwd ='', database = 'sqi_db')
# mycursor = mycon.cursor()
# mycursor.execute("CREATE TABLE customer_profile(matric_number INT(10) PRIMARY KEY, full_name VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, department VARCHAR(50) NOT NULL)")
# mycursor.execute("ALTER TABLE customer_profile ADD password VARCHAR(50) NOT NULL")
# mycon.commit()
import time
import sys 
import pwinput as pw
class Entrance_validator:
    def __init__(self):
        self.name = "Entrance Validator"
        self.landing_page()
    
    def sign_in(self):
        self.user_matric_no = input("Enter your matric number: ")
        self.user_passwd = pw.pwinput("Enter your password: ")
        
        mycon = sql.connect(host ='127.0.0.1', user ='root', passwd ='', database = 'sqi_db')
        mycursor = mycon.cursor()
        myquery = "SELECT * FROM customer_profile WHERE matric_number = %s AND password = %s"
        val = (self.user_matric_no, self.user_passwd)
        mycursor.execute(myquery, val)
        # # self.myquery = "SELECT * FROM customer_profile WHERE matric_number = %s AND password = %s"
        # # self.val = (self.user_matric_no, self.user_passwd)
        # mycursor.execute(self.myquery, self.val)
        self.user_details = mycursor.fetchall()
        
        
        if self.user_details:
            print(""" Login successful...
                      Welcome to SQI College of ICT
                                                    We're glad you're here...
                                    I am the entrance validator henceforth, please identify yourself:
                                                1. Student
                                                2. Staff
                                                3. Parent/Guardian
                                                4. Freelancer
                                                5. Alumnus 
                    """)
             
            time.sleep(3)
            print("Please wait...")
            self.user = input("Please enter the correspondence 1/2.../6: ")
            
            if self.user == "1": 
                print("""Please enter your dsicipline: 
                            1. Data science
                            2. Data analytics
                            3. Web development
                            4. Product management
                            5. Graphic design
                            6. UI/UX design
                            """)
                self.option = input("Please enter the correspondence 1/2.../6: ")
                if self.option == "1":
                    print("""Please select the category that applies to your tuition fee status: 
                                    1. Complete payment
                                    2. part-payment
                                    3. No payment yet
                                    4. Ready to pay 
                                    """)
                    self.option_1 = (input("Please select the correspondence 1/.../4: "))
                    if self.option_1 == "1":
                        print("Welcome dear user, your entrance is now validated. I hope you enjoy your day.")
                    elif option_1 == "2":
                        print("Your entrance has been validated, Please proceed to your respective lecture hall. However, a subtle reminder to comlete your payment as at when due. Failure to do so might nullify your entrance to the lecture room. Have a great day.") 
                    elif option_1 == "3":
                        print("Your entrance has not been validated, Please proceed to make a full or partial payment in order to have access to the college facility. Thanks")
                    elif option_1 == "4":
                        print("Please proceed to the front desk.")
                    else:
                        print("Invalid input")
                elif self.option == "2": 
                    print("""Please select the category that applies to your tuition fee status: 
                        1. Complete payment
                        2. part-payment
                        3. No payment yet
                        4. Ready to pay 
                        """)
                    option_1 = (input("Please select the correspondence 1/.../4: "))
                    if option_1 == "1":
                        print("Welcome dear user, your entrance is now validated. I hope you enjoy your day.")
                    elif option_1 == "2":
                        print("Your entrance has been validated, Please proceed to your respective lecture hall. However, a subtle reminder to comlete your payment as at when due. Failure to do so might nullify your entrance to the lecture room. Have a great day.") 
                    elif option_1 == "3":
                        print("Your entrance has not been validated, Please proceed to make a full or partial payment in order to have access to the college facility. Thanks")
                    elif option_1 == "4":
                        print("Please proceed to the front desk.")
                    else:
                        print("Invalid input")
                elif self.option == "3":
                    print("""Please select the category that applies to your tuition fee status: 
                        1. Complete payment
                        2. part-payment
                        3. No payment yet
                        4. Ready to pay 
                        """)
                    option_1 = (input("Please select the correspondence 1/.../4: "))
                    if option_1 == "1":
                        print("Welcome dear user, your entrance is now validated. I hope you enjoy your day.")
                    elif option_1 == "2":
                        print("Your entrance has been validated, Please proceed to your respective lecture hall. However, a subtle reminder to comlete your payment as at when due. Failure to do so might nullify your entrance to the lecture room. Have a great day.") 
                    elif option_1 == "3":
                        print("Your entrance has not been validated, Please proceed to make a full or partial payment in order to have access to the college facility. Thanks")
                    elif option_1 == "4":
                        print("Please proceed to the front desk.")
                    else:
                        print("Invalid input")
                elif self.option == "4":
                    print("""Please select the category that applies to your tuition fee status: 
                        1. Complete payment
                        2. part-payment
                        3. No payment yet
                        4. Ready to pay 
                        """)
                    option_1 = (input("Please select the correspondence 1/.../4: "))
                    if option_1 == "1":
                        print("Welcome dear user, your entrance is now validated. I hope you enjoy your day.")
                    elif option_1 == "2":
                        print("Your entrance has been validated, Please proceed to your respective lecture hall. However, a subtle reminder to comlete your payment as at when due. Failure to do so might nullify your entrance to the lecture room. Have a great day.") 
                    elif option_1 == "3":
                        print("Your entrance has not been validated, Please proceed to make a full or partial payment in order to have access to the college facility. Thanks")
                    elif option_1 == "4":
                        print("Please proceed to the front desk.")
                    else:
                        print("Invalid input")
                elif self.option == "5":
                    print("""Please select the category that applies to your tuition fee status: 
                        1. Complete payment
                        2. part-payment
                        3. No payment yet
                        4. Ready to pay 
                        """)
                    option_1 = (input("Please select the correspondence 1/.../4: "))
                    if option_1 == "1":
                        print("Welcome dear user, your entrance is now validated. I hope you enjoy your day.")
                    elif option_1 == "2":
                        print("Your entrance has been validated, Please proceed to your respective lecture hall. However, a subtle reminder to comlete your payment as at when due. Failure to do so might nullify your entrance to the lecture room. Have a great day.") 
                    elif option_1 == "3":
                        print("Your entrance has not been validated, Please proceed to make a full or partial payment in order to have access to the college facility. Thanks")
                    elif option_1 == "4":
                        print("Please proceed to the front desk.")
                    else:
                        print("Invalid input")
                elif self.option == "6":
                    print("""Please select the category that applies to your tuition fee status: 
                        1. Complete payment
                        2. part-payment
                        3. No payment yet
                        4. Ready to pay 
                        """)
                    option_1 = (input("Please select the correspondence 1/.../4: "))
                    if option_1 == "1":
                        print("Welcome dear user, your entrance is now validated. I hope you enjoy your day.")
                    elif option_1 == "2":
                        print("Your entrance has been validated, Please proceed to your respective lecture hall. However, a subtle reminder to comlete your payment as at when due. Failure to do so might nullify your entrance to the lecture room. Have a great day.") 
                        self.landing_page()
                    elif option_1 == "3":
                        print("Your entrance has not been validated, Please proceed to make a full or partial payment in order to have access to the college facility. Thanks")
                    elif option_1 == "4":
                        print("Please proceed to the front desk.")
                    else:
                        print("Invalid input")
                else: 
                    print("Invalid option")
                    
    def sign_up(self):
        print("Welcome to SQI College of ICT, Please enter the following details to sign up")
        self.user_matric = input("Enter your Matric number: ")
        self.user_name = input("Enter your full name: ")
        self.user_email = input("Enetr your email: ")
        self.user_depart = input("Enter your department: ")
        self.user_password = input("Enter your password: ")
        
        
        mycon = sql.connect(host ='127.0.0.1', user ='root', passwd ='', database = 'sqi_db')
        mycursor = mycon.cursor()
        self.db_query = "INSERT INTO customer_profile (matric_number, full_name, email, department, password) VALUES (%s, %s, %s, %s, %s)"  
        self.val = (self.user_matric, self.user_name, self.user_email, self.user_depart, self.user_password)
        mycursor.execute(self.db_query, self.val)
        mycon.commit()
        mycon.close()
        
        user_resp = input("Please press 0 to quit or 1 to sign in: ")
        print("Please wait...")
        time.sleep(3)
        if user_resp == "1":
            self.sign_in()
        elif user_resp == 0:
            sys.exit()
            
    def landing_page(self):
        print("""
                                                Welcome to SQI College of ICT
                                                We're glad you're here...
                    I am the entrance validator henceforth, please select the operation you'd like to perform: 
                                                    1. Sign in
                                                    2. Sign up
                                                    3. Exit
                                                    """)
        user_inp = input("Enter your response: ")
        # try:
        if user_inp == "1":
            self.sign_in()
        elif user_inp == "2":
            self.sign_up()
        elif user_inp == "3":
            sys.exit()
        else:
            print("Invalid Response")
            self.landing_page()
        # except TypeError:
            # print("Please enter a valid response")
            # self.landing_page()

user_1 = Entrance_validator()
