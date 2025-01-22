"""
File: instructorExec.py

Description:
This script manages the login functionality for instructors, post-login operations,
and instructor menu navigation. It includes utilities for verifying credentials, retrieving
assigned classes, and providing options for viewing classes or logging out.

Dependencies:
- Python Standard Library: os, sys
- Custom Modules: Instructor (from instructorClass), mainUtil (from Utility)

Functionality:
1. Handles instructor login with a maximum of 5 attempts.
2. Redirects logged-in instructors to a menu for viewing their classes or logging out.
3. Retrieves and displays the classes assigned to the instructor.

Structure:
- login(): Facilitates login attempts and authentication.
- postLogin(): Manages post-login initialization and menu redirection.
- retrieveClasses(): Fetches the classes associated with the instructor from CSV files.
- instructMenu(): Provides a menu-driven interface for instructor actions.

Usage:
Run the script to prompt instructors for login credentials, access their classes, or manage their accounts.

Author:
Van Robbins

Date Created:
2024-12-3

Last Updated:
2024-12-10

Version 1.0
"""
import os;
import sys;
from instructorClass import Instructor;
# Get the absolute path of the Project directory (parent of User and Utility)
projectDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"));
# Add the Project directory to sys.path
if projectDir not in sys.path:
    sys.path.insert(0, projectDir);
try:
    from Utility import mainUtil
    from Courses.courseClass import Course
except:
    print("Module not found");


def login():
    """
    Handles the instructor login functionality. The user has up to 5 attempts to log in successfully.
    On success, the user is redirected to the post-login menu.
    """
    loginAttempt = 0;  # Counter for login attempts
    enterLogin = ["<username>", "<password>"];  # Placeholder for username and password
    tryLogin = [False, loginAttempt];  # Tracks login success and attempts count
    print("Instructor Login");  # Display the login prompt
    filePath = os.path.join(projectDir, "Users", "Instructor", "InstructorData", "instructorLogin.csv");
    # Create and initialize the CSV file if it doesn't exist
    if not os.path.isfile(filePath):
        print("No Instructors added yet!");
        quit();
    # Loop until login is successful or attempts exceed 5
    while tryLogin[0] == False and loginAttempt < 5:
        enterLogin[0] = input("Enter Username: ");  # Prompt for username
        enterLogin[1] = input("Enter Password: ");  # Prompt for password

        # Attempt login using mainUtil's login method
        tryLogin = mainUtil.login(os.path.join(os.getcwd(), "Users", "Instructor", "InstructorData", "instructorLogin.csv"),3,4,enterLogin,loginAttempt);
        loginAttempt = tryLogin[1];  # Update login attempt count

    print("Login Successful");  # Notify successful login
    postLogin(tryLogin[2][:4]);  # Pass the user data to post-login

def postLogin(loginUser):
    """
    Handles post-login operations, initializes the global logged-in instructor, and redirects to the instructor menu.
    """
    global loggedInUser;  # Declare global variable for the logged-in instructor
    loggedInUser = Instructor(loginUser[0], loginUser[1], loginUser[3]);
    loggedInUser.setTite(loginUser[2]);  # Initialize instructor object
    loggedInUser.setClasses(retrieveClasses(loggedInUser.getUsername()));
    print(f"Welcome {loggedInUser.getFirstNm()}!");  # Greet the instructor
    instructMenu();  # Redirect to the instructor menu


def instructMenu():
    """
    Main menu for instructor actions such as viewing classes or logging out.
    """
    print("What would you like to do?");  # Prompt instructor for their choice
    options = ["View Your Classes", "Logout"];  # Menu options
    selection = mainUtil.menu(options,True);  # Display menu and capture selection

    if selection == 1:
        viewInstructClass();
        instructMenu();
    else:
        print("Successfully logged out");  # Notify logout
        print("Login to different account?");  # Ask if they want to log in again
        options = ["Login Again"];  # Provide login option
        selection = mainUtil.menu(options, True);  # Display menu and capture selection
        if selection == 1:
            login();  # Redirect to login
def retrieveClasses(userName):
    """
    Fetches the classes associated with the instructor from the course information file.
    Returns a list of Course objects.
    """
    courses=[]
    mainUtil.initializeCSV(os.path.join(projectDir, "Courses"), "courseInfo.csv", ["CourseNumber", "CourseName", "Instructor"]);
    coursesData = mainUtil.csvToArray(os.path.join(projectDir, "Courses", "courseInfo.csv"), True);
    instructorsClasses = mainUtil.parseArray(coursesData, userName, 2, None);
    if instructorsClasses!=None:
        for row in instructorsClasses:  # Get rows where instructor matches
            courses = [Course(row[0], row[1], row[2])];  # Create Course objects for matched rows
    return courses;
def viewInstructClass():
    """
    Gets instructor classes and prints them out in list
    """
    instructClasses = loggedInUser.getClasses();  # Get the list of Course objects
    print(f"{loggedInUser.getTitleName()}'s Courses:");  # Print instructor title and name
    for course in instructClasses:
        print({course});
        
# Start the login process
login();
