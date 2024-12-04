#Password Management Script
Password Management Script
Description
This Python script is a simple password management tool. It allows users to securely view stored account details, add new accounts, and modify existing ones. It uses a pin-based authentication system for extra security.

Features:
PIN Authentication: Before any action is allowed, users must enter the correct pin.
View Account Details: View all stored account names and passwords (from the password.txt file).
Change Account Details: Add a new account name and password to the file.
Exit: Quit the program with a 'q' command.
Requirements:
Python 3.x
A file named password.txt in the same directory to store the account data. This file should initially be empty or contain existing account details in the following format:
Copy code
account_name|password
How it works:
PIN Authentication:

When you run the script, it asks for a pin.
The correct pin is 2005. If the pin entered is incorrect, the script will print "Invalid pin" and exit.
Main Menu:

After authentication, the script presents a menu with three options:
view: View all stored account details.
change: Add a new account or modify an existing one.
q: Quit the program.
Viewing Accounts:

The script will read from the password.txt file and display all account names and passwords stored there.
Each account is stored in the format account_name|password.
Editing Accounts:

You can add a new account by providing a name and a strong password.
The new details are appended to the password.txt file.
Exiting:

To exit the program, simply type q.
Usage:
Clone or download the script to your local machine.
Ensure the password.txt file is in the same directory as the script.
Run the script using Python:
bash
Copy code
python password_manager.py
Follow the on-screen prompts to authenticate and interact with the script.
Example:
Sample Run:
bash
Copy code
$ python password_manager.py
What's the pin? : 2005
Would you like to view account, edit details, or delete account (view, change, q)? Press 'q' to exit: view
account1|password123
account2|securepass456

Would you like to view account, edit details, or delete account (view, change, q)? Press 'q' to exit: change
Add the account name: new_account
Create a strong password!: mynewpassword
The details have been edited!

Would you like to view account, edit details, or delete account (view, change, q)? Press 'q' to exit: view
account1|password123
account2|securepass456
new_account|mynewpassword

Would you like to view account, edit details, or delete account (view, change, q)? Press 'q' to exit: q
Notes:
The passwords stored are not encrypted and should not be used for storing sensitive data in a production environment.
Make sure the password.txt file is kept secure and is not accessible to unauthorized users.
License:
This script is provided for educational purposes only. Feel free to modify and use it for personal use. For any commercial use, please ensure appropriate security measures are implemented, such as encrypting stored passwords.
