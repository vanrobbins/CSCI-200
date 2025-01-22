"""
Registrar System Entry Point
This script serves as the entry point for the Registrar System, allowing users to select their role (Student, Instructor, or Admin) 
and redirecting them to the appropriate functionality.

Imports:
    - os: For executing role-specific scripts.
    - mainUtil (from Utility): For utility functions like menu display and selection handling.
Author:
Van Robbins

Date Created:
2024-12-3

Last Updated:
2024-12-10

Version 1.0
"""

import os;  # Importing OS module to run role-specific scripts
import Utility.mainUtil as mainUtil;  # Importing main utility functions from Utility package

# Welcome message for the user
print("Welcome To The Registrar\nSelect User Type");

# Define main menu options for user types
mainMenu = ["Student", "Instructor", "Admin"];  # List of user roles
selectedOption = mainUtil.menu(mainMenu,True);  # Display menu and capture user selection

# Redirect based on user selection
if selectedOption == 1:
    os.system('python Users/Student/studentExec.py');  # Redirect to Student module
elif selectedOption == 2:
    os.system('python Users/Instructor/instructorExec.py');  # Redirect to Instructor module
elif selectedOption == 3:
    os.system("python Users/Admin/adminExec.py");  # Redirect to Admin module
else:
    print("This shouldn't be possible...");  # Print error message if the selection is invalid
    quit();  # Exit the script