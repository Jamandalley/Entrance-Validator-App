# School Entrance Validation App
The School Entrance Validation App is a Python-based application designed to facilitate secure and efficient entrance validation for students at SQI College of ICT. The app interacts with a MySQL database to manage student profiles and streamline the entrance validation process.

# Features
Secure Entrance Validation: Validate student entrance based on matriculation number and password.

# User Registration: 
New students can register by providing essential details such as matriculation number, full name, email, department, and password.

# Database Integration: 
Utilizes MySQL database for secure storage of student profiles and entrance validation records.

# Table of Contents
1. Installation
2. Getting Started
3. Usage
4. Contributing
5. License

## Installation
Clone the repository:
`git clone https://github.com/your-username/school-entrance-validation-app.git`

## Navigate to the project directory:
`cd school-entrance-validation-app`

## Set up the MySQL database:
Ensure MySQL server is running.
Modify the database connection details in the script (`mycon = sql.connect(...)`) as needed.
Run the script to create the necessary database and tables.

# Getting Started
## Run the application:
`python entrance_validator.py`

## Access the application through the command line interface.
# Usage
Sign In
Enter your matriculation number.
Enter your password securely using pwinput.
The app will validate your entrance and prompt you to select your user category.

Sign Up
Choose the "Sign Up" option from the landing page.
Enter your matriculation number, full name, email, department, and password.
Complete the registration process.

# Landing Page
The landing page provides options for signing in, signing up, or exiting the application.
Invalid responses are handled with appropriate messages.

# Contributing
Contributions to the School Entrance Validation App are welcome. Please follow the Contributing Guidelines for details on how to contribute to this project.
