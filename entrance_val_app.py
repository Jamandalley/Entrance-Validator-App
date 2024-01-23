import mysql.connector as sql
import time
import sys 
import pwinput as pw
from tkinter import *
from tkinter import messagebox

class Entrance_validator:
    def __init__(self, window):
        self.mycon = sql.connect(host ='127.0.0.1', user ='root', passwd ='', database = 'sqi_db')
        self.mycursor = self.mycon.cursor()
        self.window = window
        self.window.title("SQI College of ICT Entrance Validator App")
        self.window.geometry("850x520")
        self.window.minsize(800, 400)
        self.window.config(bg="#87BDD8")
        
        self.user_matric_no = StringVar()
        self.user_passwd = StringVar()

        Label(self.window, text="Enter your matric number:").grid(row=0, column=0)
        Entry(self.window, textvariable=self.user_matric_no).grid(row=0, column=1)

        Label(self.window, text="Enter your password:").grid(row=1, column=0)
        Entry(self.window, textvariable=self.user_passwd, show="*").grid(row=1, column=1)

        Button(self.window, text="Sign In", command=self.sign_in_page).grid(row=2, column=0)
        Button(self.window, text="Sign Up", command=self.sign_up_page).grid(row=2, column=1)
    
    def sign_in_page(self):
        matric_number = self.user_matric_no.get()
        password = self.user_passwd.get()

        mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='sqi_db')
        mycursor = mycon.cursor()
        myquery = "SELECT * FROM customer_profile WHERE matric_number = %s AND password = %s"
        val = (matric_number, password)
        mycursor.execute(myquery, val)
        user_details = mycursor.fetchall()

        if user_details:
            self.window.destroy()
            self.validate_entrance(user_details)
        else:
            messagebox.showerror("Error", "Invalid matric number or password")

    def validate_entrance(self, user_details):
        # create a new window for entrance validation
        self.window = Tk()
        self.window.title("Entrance Validation")

        # display welcome message
        Label(self.window, text="Welcome to SQI College of ICT!\nWe're glad you're here...").grid(row=0, column=0, columnspan=2)

        # get user type
        user_type = StringVar()
        Label(self.window, text="Please select your user type:").grid(row=1, column=0)
        Radiobutton(self.window, text="Student", variable=user_type, value="student").grid(row=2, column=0)
        Radiobutton(self.window, text="Staff", variable=user_type, value="staff").grid(row=3, column=0)
        Radiobutton(self.window, text="Parent/Guardian", variable=user_type, value="parent").grid(row=4, column=0)
        Radiobutton(self.window, text="Freelancer", variable=user_type, value="freelancer").grid(row=5, column=0)
        Radiobutton(self.window, text="Alumnus", variable=user_type, value="alumnus").grid(row=6, column=0)

        # display tuition fee options
        tuition_fee_status = StringVar()
        Label(self.window, text="Please select your tuition fee status:").grid(row=1, column=1)
        Radiobutton(self.window, text="Complete payment", variable=tuition_fee_status, value="paid").grid(row=2, column=1)
        Radiobutton(self.window, text="Part payment", variable=tuition_fee_status, value="partial").grid(row=3, column=1)
        Radiobutton(self.window, text="No payment yet", variable=tuition_fee_status, value="unpaid").grid(row=4, column=1)
        Radiobutton(self.window, text="Ready to pay", variable=tuition_fee_status, value="ready").grid(row=5, column=1)

        # validate entrance button
        Button(self.window, text="Validate Entrance", command=lambda: self.validate_entrance_command(user_details, user_type.get(), tuition_fee_status.get())).grid(row=6, column=1)

    def validate_entrance_command(self, user_details, user_type, tuition_fee_status):
        self.entrance_window = Toplevel(self.window)
        self.entrance_window.title("Entrance Page")
        self.entrance_window.geometry("300x250")
        self.entrance_window.config(bg="#87BDD8")
        # do validation logic here
        if user_type == "Student":
            self.tuition_status_label = Label(self.entrance_window, text= f"User type: {user_type}, Tuition fee status: {tuition_fee_status}")
            self.tuition_status_label.pack(pady=10)
                
            self.user_details_label = Label(self.entrance_window, text=f"User details: {user_details}") 
            self.user_details_label.pack(pady=10)
                
            if tuition_fee_status == 'paid':
                self.entrance_message = Label(self.entrance_window, text="Welcome dear user, your entrance is now validated. I hope you enjoy your day.")
                self.entrance_message.pack(pady=10)
                
            elif tuition_fee_status == 'partial':
                self.entrance_message = Label(self.entrance_window, text="Your entrance has been validated, Please proceed to your respective lecture hall. However, a subtle reminder to comlete your payment as at when due. Failure to do so might nullify your entrance to the lecture room. Have a great day.")
                self.entrance_message.pack(pady=10)
                
            elif tuition_fee_status == "unpaid":
                self.entrance_message = Label(self.entrance_window, text="Your entrance has not been validated, Please proceed to make a full or partial payment in order to have access to the college facility. Thanks")
                self.entrance_message.pack(pady=10)
            
            elif tuition_fee_status == "ready":
                self.entrance_message(self.entrance_window, text="Please proceed to the front desk.")
                self.entrance_message.pack(pady=10)
                
            else:
                messagebox.showerror("Error", "Invalid Entry")
        
        elif user_type == "staff":
            pass
        
        elif user_type == "parent":
            pass
        
        elif user_type == "freelancer":
            pass
        
        elif user_type == "alumnus":
            pass 
        
        else:
            messagebox.showerror("Error", "Invalid Entry")
                    
    def sign_up_page(self):
        self.sign_up_window = Toplevel(self.window)
        self.sign_up_window.title("Sign Up")
        self.sign_up_window.geometry("300x490")
        self.sign_up_window.config(bg="#87BDD8")

        self.sign_up_matric_entry_label = Label(self.sign_up_window, text="Matric Number:", 
                                                font=("Times New Roman", 10))
        self.sign_up_matric_entry = Entry(self.sign_up_window, font="calibre 15")
        self.sign_up_matric_entry_label.pack(pady=5)
        self.sign_up_matric_entry.pack(pady=10)

        self.sign_up_username_entry_label = Label(self.sign_up_window, text="Full Name:", 
                                                  font=("Times New Roman", 10))
        self.sign_up_username_entry = Entry(self.sign_up_window, font="calibre 15")
        self.sign_up_username_entry_label.pack(pady=5)
        self.sign_up_username_entry.pack(pady=10)

        self.sign_up_email_entry_label = Label(self.sign_up_window, text="Email:", 
                                                  font=("Times New Roman", 10))
        self.sign_up_email_entry = Entry(self.sign_up_window, font="calibre 15")
        self.sign_up_email_entry_label.pack(pady=5)
        self.sign_up_email_entry.pack(pady=10)
        
        self.sign_up_department_entry_label = Label(self.sign_up_window, text="Department:", 
                                                  font=("Times New Roman", 10))
        self.sign_up_department_entry = Entry(self.sign_up_window, font="calibre 15")
        self.sign_up_department_entry_label.pack(pady=5)
        self.sign_up_department_entry.pack(pady=10)

        self.sign_up_password_entry_label = Label(self.sign_up_window, text="Password:", 
                                                  font=("Times New Roman", 10))
        self.sign_up_password_entry = Entry(self.sign_up_window, font="calibre 15", show="*")
        self.sign_up_password_entry_label.pack(pady=5)
        self.sign_up_password_entry.pack(pady=10)

        self.sign_up_button = Button(self.sign_up_window, 
                                     text="Sign Up", 
                                     command=lambda: self.save_user(self.sign_up_matric_entry.get(), 
                                                                    self.sign_up_username_entry.get(), 
                                                                    self.sign_up_email_entry.get(),
                                                                    self.sign_up_department_entry.get(),
                                                                    self.sign_up_password_entry.get()))
        self.sign_up_button.pack(pady=10)

    def save_user(self, matric_no, username, email, department, password):
        query_1 = "SELECT * FROM customer_profile WHERE matric_number = %s"
        val_1 = (matric_no,)
        self.mycursor.execute(query_1, val_1)
        user_details = self.mycursor.fetchall()
        if user_details:
            Label(self.sign_up_window, text="Matriculation number already exists", font="calibre 12").pack()
            messagebox.showerror('Error', 'User already exists!')
        else:
            db_query = "INSERT INTO customer_profile(matric_number, full_name, email, department, password) VALUES (%s, %s, %s, %s, %s)"  
            val = (matric_no, username, email, department, password)
            self.mycursor.execute(db_query, val)
            self.mycon.commit()
            messagebox.showinfo("Signup Successful", "Account created successfully. You can now login.")
            self.sign_up_window.destroy()

window = Tk()
user_1 = Entrance_validator(window)
window.mainloop()