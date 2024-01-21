import tkinter as tk
from tkinter import messagebox
import mysql.connector as sql
import time
import pwinput as pw
import hashlib

class EntranceValidator:
    def __init__(self):
        self.mycon = None
        self.mycursor = None

    def connect_to_database(self):
        self.mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database='sqi_db')
        self.mycursor = self.mycon.cursor()

    def sign_up(self, matric_no, name, email, department, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        myquery = "INSERT INTO customer_profile (matric_number, name, email, department, password) VALUES (%s, %s, %s, %s, %s)"
        val = (matric_no, name, email, department, hashed_password)
        self.mycursor.execute(myquery, val)
        self.mycon.commit()

    def validate_login(self, matric_no, password):
        myquery = "SELECT * FROM customer_profile WHERE matric_number = %s"
        val = (matric_no, )
        self.mycursor.execute(myquery, val)
        user_details = self.mycursor.fetchone()

        if user_details and pw.verify(password.encode(), user_details[4].encode()):
            return True
        else:
            return False

class EntranceValidatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SQI College Entrance Validator")
        self.geometry("400x300")
        self.entrance_validator = EntranceValidator()
        self.connect_to_database()

        # Create widgets
        self.label = tk.Label(self, text="Welcome to SQI College Entrance Validator", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.sign_in_button = tk.Button(self, text="Sign In", command=self.show_sign_in)
        self.sign_in_button.pack(pady=5)

        self.sign_up_button = tk.Button(self, text="Sign Up", command=self.show_sign_up)
        self.sign_up_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.pack(pady=5)

    def connect_to_database(self):
        self.entrance_validator.connect_to_database()

    def show_sign_in(self):
        self.withdraw()  # Hide the main window
        self.sign_in_window = SignInWindow(self, self.entrance_validator)
        self.sign_in_window.grab_set()

    def show_sign_up(self):
        self.withdraw()  # Hide the main window
        self.sign_up_window = SignUpWindow(self, self.entrance_validator)
        self.sign_up_window.grab_set()

class SignInWindow(tk.Toplevel):
    def __init__(self, master, entrance_validator):
        super().__init__(master)
        self.title("Sign In")
        self.geometry("300x200")
        self.entrance_validator = entrance_validator

        # Create widgets
        self.matric_label = tk.Label(self, text="Matric Number:")
        self.matric_entry = tk.Entry(self)
        self.matric_label.pack(pady=5)
        self.matric_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.password_label.pack(pady=5)
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.validate_login)
        self.login_button.pack(pady=10)

    def validate_login(self):
        matric_no = self.matric_entry.get()
        password = self.password_entry.get()

        if self.entrance_validator.validate_login(matric_no, password):
            messagebox.showinfo("Login Successful", "Welcome to SQI College!")
            self.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid Matric Number or Password")

class SignUpWindow(tk.Toplevel):
    def __init__(self, master, entrance_validator):
        super().__init__(master)
        self.title("Sign Up")
        self.geometry("300x250")
        self.entrance_validator = entrance_validator

        # Create widgets
        self.matric_label = tk.Label(self, text="Matric Number:")
        self.matric_entry = tk.Entry(self)
        self.matric_label.pack(pady=5)
        self.matric_entry.pack(pady=5)

        self.name_label = tk.Label(self, text="Full Name:")
        self.name_entry = tk.Entry(self)
        self.name_label.pack(pady=5)
        self.name_entry.pack(pady=5)

        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self)
        self.email_label.pack(pady=5)
        self.email_entry.pack(pady=5)

        self.department_label = tk.Label(self, text="Department:")
        self.department_entry = tk.Entry(self)
        self.department_label.pack(pady=5)
        self.department_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.password_label.pack(pady=5)
        self.password_entry.pack(pady=5)

        self.signup_button = tk.Button(self, text="Sign Up", command=self.validate_signup)
        self.signup_button.pack(pady=10)

    def validate_signup(self):
        matric_no = self.matric_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        department = self.department_entry.get()
        password = self.password_entry.get()

        if matric_no and name and email and department and password:
            self.entrance_validator.sign_up(matric_no, name, email, department, password)
            messagebox.showinfo("Sign Up Successful", "You have successfully signed up!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all the fields")

if __name__ == "__main__":
    app = EntranceValidatorApp()
    app.mainloop()