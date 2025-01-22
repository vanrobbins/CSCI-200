"""
File: adminExec.py

Description:
This script manages the login functionality for admins, post-login operations,
and admin menu navigation. It includes utilities for verifying credentials, 
managing students, instructors, and courses, as well as viewing and modifying data.

Dependencies:
- Python Standard Library: os, sys
- Custom Modules: Admin (from adminClass), Instructor (from Users.Instructor.instructorClass), mainUtil (from Utility)

Functionality:
1. Handles admin login with a maximum of 5 attempts.
2. Redirects logged-in admins to a menu for managing data or logging out.
3. Provides options to add, view, or update data for students, instructors, and courses.

Structure:
- login(): Facilitates login attempts and authentication for admins.
- postLogin(): Manages post-login initialization and redirects to the admin menu.
- adminMenu(): Provides a menu-driven interface for admin actions.
- addMenu(): Handles the addition of students, instructors, or courses.
- viewMenu(): Allows viewing of registered data for students, instructors, courses, or enrollments.

Usage:
Run the script to prompt admins for login credentials, manage data, or view details.

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
from adminClass import Admin;
# Get the absolute path of the Project directory (parent of User and Utility)
projectDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# Add the Project directory to sys.path
if projectDir not in sys.path:
    sys.path.insert(0, projectDir);
try:
    from Utility import mainUtil
    from Users.Instructor.instructorClass import Instructor;
except:
    print("Module not found")


def login():
    """
    Handles the admin login functionality. The user has up to 5 attempts to log in successfully.
    On success, the user is redirected to the post-login menu.
    """
    loginAttempt = 0;  # Counter for login attempts
    enterLogin = ["<username>", "<password>"];  # Placeholder for username and password
    tryLogin = [False, loginAttempt];  # Tracks login success and attempts count
    print("Admin Login");  # Display the login prompt

    # Loop until login is successful or attempts exceed 5
    while tryLogin[0] == False and loginAttempt < 5:
        enterLogin[0] = input("Enter Username: ");  # Prompt for username
        enterLogin[1] = input("Enter Password: ");  # Prompt for password

        # Attempt login using mainUtil's login method
        tryLogin = mainUtil.login(os.path.join(os.getcwd(), "Users", "Admin", "AdminData", "adminLogin.csv"),2,3,enterLogin,loginAttempt);
        loginAttempt = tryLogin[1];  # Update login attempt count

    print("Login Successful");  # Notify successful login
    postLogin(tryLogin[2][:3]);  # Pass the user data to post-login menu

def postLogin(loginUser):
    """
    Handles post-login operations, initializes the global logged-in admin, and redirects to admin menu.
    """
    global loggedInUser;  # Declare global variable for the logged-in user
    loggedInUser = Admin(loginUser[0], loginUser[1], loginUser[2]);  # Initialize admin object
    print(f"Welcome {loggedInUser.getFirstNm()}!");  # Greet the admin
    adminMenu();  # Redirect to the admin menu

def adminMenu():
    """
    Main menu for admin actions such as adding data, viewing data, or logging out.
    """
    print("What would you like to do?");  # Prompt admin for their choice
    options = ["Add", "View", "Logout"];  # Menu options
    selection = mainUtil.menu(options,True);  # Display menu and capture selection

    if selection == 1:
        addMenu();  # Redirect to the add menu
    elif selection == 2:
        viewMenu();  # Redirect to the view menu
    else:
        print("Successfully logged out");  # Notify logout
        print("Login to different account?");  # Ask if they want to log in again
        options = ["Login Again"];  # Provide login option
        selection = mainUtil.menu(options, True);  # Display menu and capture selection
        if selection == 1:
            login();  # Redirect to login

def addMenu():
    """
    Provides admin options to add students, instructors, or courses, or go back to the main menu.
    """
    print("Add to Registrar");  # Notify admin about the add menu
    options = ["Add Students", "Add Instructor", "Add Course", "Back to Main Menu"];  # Menu options
    selection = mainUtil.menu(options,True);  # Display menu and capture selection

    if selection == 1:
        # Initialize student CSV and redirect to add student menu
        mainUtil.initializeCSV(os.path.join(projectDir, "Users", "Student", "StudentData"),"studentLogin.csv",
                                ["FirstName", "LastName", "Username", "Password"]);
        addStudent();  # Add a new student
    elif selection == 2:
        # Initialize instructor CSV and redirect to add instructor menu
        mainUtil.initializeCSV(os.path.join(projectDir, "Users", "Instructor", "InstructorData"),"instructorLogin.csv",
                                ["FirstName", "LastName", "Title", "Username", "Password"]);
        addInstruct();  # Add a new instructor
    elif selection == 3:
        # Initialize course CSV and redirect to add course menu
        mainUtil.initializeCSV(os.path.join(projectDir, "Courses"),"courseInfo.csv",
                            ["CourseNumber", "CourseName", "Instructor"]);
        addCourse();  # Add a new course
    else:
        adminMenu();  # Go back to the admin menu

def addStudent():
    """
    Function to add a new student to the system. 
    The function collects first name, last name, username, and password, validates each input, 
    checks for username uniqueness, and then saves the data to a CSV file.
    """
    print("Add Student");
    # Initialize new student data with placeholders
    newStudent=["<First>","<Last>","<Username>","<Password>"];
    # Initialize validation flags
    checkFNm = False;
    checkLNm = False;
    checkUNm = False;
    checkUNmUnique = False;
    checkPW = False;
    # Validate and collect the first name
    while checkFNm==False:
        firstNm=input("First Name: ");
        # Check if the first name is valid (e.g., correct length and format)
        checkFNm=mainUtil.checkValid(firstNm,2,15,True,False,False);
    newStudent[0]=firstNm; # Store validated first name

    # Validate and collect the last name
    while checkLNm==False:
        lastNm=input("Last Name: ");
        # Check if the last name is valid (e.g., correct length and format)
        checkLNm=mainUtil.checkValid(lastNm,2,15,True,False,False);
    newStudent[1]=lastNm;# Store validated last name

    # Validate and collect the username
    while checkUNm==False or checkUNmUnique==False:
        userNm=input("Username: ")
        checkUNm=mainUtil.checkValid(userNm,2,15,False,True,True);
        if checkUNm==False:
            continue;  # If invalid, prompt the user again
        
        # Username is valid; check if the username is unique in the data file
        checkUNmUnique=mainUtil.checkUnique(os.path.join(projectDir,"Users","Student","StudentData","studentLogin.csv"),2,userNm);
        if checkUNmUnique==False:
            print("Username not unique");# Inform user if username already exists
            mainUtil.again();# Prompt the user to try again
    newStudent[2]=userNm;# Store validated and unique username

    # Validate and collect the password
    while checkPW==False:
        passw=input("Password: ");
        # Check if the password is valid (e.g., correct length and secure format)
        checkPW=mainUtil.checkValid(passw,2,15,False,True,True);
    newStudent[3]=passw;# Store validated password

    # Add the new student data to the CSV file
    mainUtil.addToDataFile(newStudent,os.path.join(projectDir,"Users","Student","StudentData","studentLogin.csv"));
    print(f"{newStudent[2]} - {newStudent[0]} {newStudent[1]}, successfully added!");

    # Provide options to the admin for the next action
    options=["Add another student","Main Admin Menu"];
    selection=mainUtil.menu(options,True);# Display a menu and get the admin's choice
    # Handle menu selection
    if selection==1:
        addStudent();
    else:
        adminMenu();
    
def addInstruct():
    """
    Function to add a new Instructor to the system. 
    The function collects first name, last name, username, and password, validates each input, 
    checks for username uniqueness, and then saves the data to a CSV file.
    """
    print("Add Instructor");  # Notify the admin about the purpose of the current action
    
    # Initialize new Instructor data with placeholders
    newInstructor = ["<First>", "<Last>", "<Title>", "<Username>", "<Password>"];  
    
    # Initialize validation flags
    checkFNm = False;  # Validation flag for first name
    checkLNm = False;  # Validation flag for last name
    checkUNm = False;  # Validation flag for username
    checkUNmUnique = False;  # Validation flag for username uniqueness
    checkPW = False;  # Validation flag for password
    
    # Validate and collect the first name
    while checkFNm == False:
        firstNm = input("First Name: ");  # Prompt for the instructor's first name
        checkFNm = mainUtil.checkValid(firstNm, 2, 15, True, False, False);  # Validate the first name
    newInstructor[0] = firstNm;  # Store the validated first name
    
    # Validate and collect the last name
    while checkLNm == False:
        lastNm = input("Last Name: ");  # Prompt for the instructor's last name
        checkLNm = mainUtil.checkValid(lastNm, 2, 15, True, False, False);  # Validate the last name
    newInstructor[1] = lastNm;  # Store the validated last name
    
    # Prompt for instructor's title
    print("What is the instructors title");  # Ask the admin for the instructor's title
    instructorTitles = ["Professor", "Assistant Professor", "Associate Professor", "Adjunct Professor", "Lecturer", 
                        "Teaching Assistant (TA)", "Academic Advisor", "Other"];  # List of available titles
    selection = mainUtil.menu(instructorTitles, False);  # Display the menu for title selection
    title = instructorTitles[selection - 1];  # Get the selected title from the menu
    newInstructor[2] = title;  # Store the selected title in the instructor data
    
    # Validate and collect the username
    while checkUNm == False:
        userNm = input("Username: ");  # Prompt for the instructor's username
        checkUNm = mainUtil.checkValid(userNm, 2, 15, False, True, True);  # Validate the username
        if checkUNm == True:
            # Check if the username is unique in the instructor data file
            checkUNmUnique = mainUtil.checkUnique(os.path.join(projectDir, "Users", "Instructor", "InstructorData", "instructorLogin.csv"), 2, userNm);  
        if checkUNmUnique == False:
            print("Username not unique");  # Notify if the username is already taken
            mainUtil.again();  # Ask the user to try again
            checkUNm=False;
    newInstructor[3] = userNm;  # Store the validated and unique username
    
    # Validate and collect the password
    while checkPW == False:
        passw = input("Password: ");  # Prompt for the instructor's password
        checkPW = mainUtil.checkValid(passw, 2, 15, False, True, True);  # Validate the password
    newInstructor[4] = passw;  # Store the validated password
    
    # Add the new Instructor data to the CSV file
    mainUtil.addToDataFile(newInstructor, os.path.join(projectDir, "Users", "Instructor", "InstructorData", "instructorLogin.csv"));  
    print(f"{newInstructor[3]} - {newInstructor[2]} {newInstructor[0]} {newInstructor[1]}, successfully added!");  # Confirmation message
    
    # Provide options to the admin for the next action
    options = ["Add another Instructor", "Main Admin Menu"];  # Options for the admin
    selection = mainUtil.menu(options, True);  # Display a menu and get the admin's choice
    
    # Handle menu selection
    if selection == 1:
        addInstruct();  # Recursive call to add another instructor
    else:
        adminMenu();  # Return to the main admin menu

def addCourse():
    """
    Function to add a new Course to the system.
    Collects course number, course name, and instructor, validates inputs, checks for uniqueness, 
    and saves the data to a CSV file.
    """
    print("Add Course");  # Notify admin about the purpose of the current action

    # Initialize new Course data
    newCourse = ["<Course Number>", "<Course Name>", "<Instructor>"];  
    
    # Validate and collect the course number
    checkCourseNum = False;  # Validation flag for course number
    checkCourseName = False;  # Validation flag for course name
    while checkCourseNum == False:
        courseNum = input("Course Number (e.g., CS101): ");  # Prompt for course number
        checkCourseNum = mainUtil.checkValid(courseNum, 3, 7, False, True, False);  # Validate course number
        if checkCourseNum==True:
            checkCNumUnique = mainUtil.checkUnique(os.path.join(projectDir, "Courses", "courseInfo.csv"),0, courseNum);  # Check if the course number is unique
            if checkCNumUnique == False:
                print("Course number is not unique. Please try again.");  # Notify about non-unique course number
                checkCourseNum = False;  # Reset the validation flag
    newCourse[0] = courseNum;  # Store the validated course number

    # Validate and collect the course name
    
    while checkCourseName == False:
        courseNm = input("Course Name: ");  # Prompt for course name
        checkCourseName = mainUtil.checkValid(courseNm, 2, 30, True, True, False);  # Validate course name
    newCourse[1] = courseNm.upper();  # Store the validated course name

    # Select the instructor from a dropdown menu
    print("Select Instructor for this Course");  # Notify admin to select an instructor
    instructorsArray= mainUtil.csvToArray(os.path.join(projectDir, "Users", "Instructor", "InstructorData", "instructorLogin.csv"),True);
    instructorObjectsStr = []
    instructorObjects = []  
    for instructor in instructorsArray:
        instructorObject=Instructor(instructor[0],instructor[1],instructor[3]);
        instructorObject.setTite(instructor[2]);
        instructorObjects.append(instructorObject);
        instructorObjectsStr.append(str(instructorObject));
    selection = mainUtil.menu(instructorObjectsStr, False);  # Display the menu for instructor selection
    selectedInstructorUN = instructorObjects[selection - 1].getUsername();  # Get the selected instructor
    newCourse[2] = selectedInstructorUN;  # Store the selected instructor

    # Add the new Course data to the CSV file
    mainUtil.addToDataFile(
        newCourse, 
        os.path.join(projectDir, "Courses", "courseInfo.csv")
    );  
    print(f"Course {newCourse[0]} - {newCourse[1]} successfully added with {newCourse[2]} as the instructor!");  # Confirmation message

    # Provide options to the admin for the next action
    options = ["Add another Course", "Main Admin Menu"];  # Options for the admin
    selection = mainUtil.menu(options, True);  # Display the menu and get admin's choice

    # Handle menu selection
    if selection == 1:
        addCourse();  # Recursive call to add another course
    else:
        adminMenu();  # Return to the main admin menu


def viewMenu():
    print("View Registrar");
    options=["View Students","View Instructors","View Courses","View Enrollment","Back to Main Menu"];
    selection=mainUtil.menu(options,True);
    if selection==1:
        # Initialize student CSV and redirect to view students
        mainUtil.initializeCSV(os.path.join(projectDir, "Users", "Student", "StudentData"),"studentLogin.csv",
                                ["FirstName", "LastName", "Username", "Password"]);
        viewStudent();
    elif selection==2:
        mainUtil.initializeCSV(os.path.join(projectDir, "Users", "Instructor", "InstructorData"),"instructorLogin.csv",
                                ["FirstName", "LastName", "Title", "Username", "Password"]);
        viewInstruct();
    elif selection==3:
        mainUtil.initializeCSV(os.path.join(projectDir, "Courses"),"courseInfo.csv",
                            ["CourseNumber", "CourseName", "Instructor"]);
        viewCourse();
    elif selection==4:
        mainUtil.initializeCSV(os.path.join(projectDir, "Courses"),"courseEnroll.csv",
                            ["Student","CourseNumber"]);
        viewEnroll();
    
    else:
        adminMenu();

def viewStudent():
    allStudents=mainUtil.csvToArray(os.path.join(projectDir, "Users", "Student", "StudentData","studentLogin.csv"),False);
    mainUtil.printTable(allStudents[0],allStudents[1:])
    viewPost();

def viewInstruct():
    allInstructors=mainUtil.csvToArray(os.path.join(projectDir, "Users", "Instructor", "InstructorData","instructorLogin.csv"),False);
    mainUtil.printTable(allInstructors[0],allInstructors[1:]);
    viewPost();

def viewCourse():
    allCourses=mainUtil.csvToArray(os.path.join(projectDir, "Courses","courseInfo.csv"),False);
    mainUtil.printTable(allCourses[0],allCourses[1:]);
    viewPost();

def viewEnroll():
    allEnrolled=mainUtil.csvToArray(os.path.join(projectDir, "Courses","courseEnroll.csv"),False);
    mainUtil.printTable(allEnrolled[0],allEnrolled[1:]);
    viewPost();

def viewPost():
    print("");
    options = ["View Something Else", "Main Admin Menu"];  # Options for the admin
    selection = mainUtil.menu(options, True);  # Display the menu and get admin's choice
    # Handle menu selection
    if selection == 1:
        viewMenu();  # Recursive call to add another course
    else:
        adminMenu();  # Return to the main admin menu

login();