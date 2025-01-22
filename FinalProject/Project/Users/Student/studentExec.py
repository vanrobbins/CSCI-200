"""
File: studentExec.py

Description:
This script manages the login functionality for students, post-login operations,
and student menu navigation. It includes utilities for verifying credentials, retrieving
assigned classes, and providing options for viewing classes or logging out.

Dependencies:
- Python Standard Library: os, sys
- Custom Modules: student (from studentClass), mainUtil (from Utility)

Functionality:
1. Handles student login with a maximum of 5 attempts.
2. Redirects logged-in students to a menu for viewing their classes or logging out.
3. Retrieves and displays the classes assigned to the student.

Structure:
- login(): Facilitates login attempts and authentication.
- postLogin(): Manages post-login initialization and menu redirection.
- retrieveClasses(): Fetches the classes associated with the student from CSV files.
- studentMenu(): Provides a menu-driven interface for student actions.

Usage:
Run the script to prompt students for login credentials, access their classes, or manage their accounts.

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
from studentClass import Student;
# Get the absolute path of the Project directory (parent of User and Utility)
projectDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"));
# Add the Project directory to sys.path
if projectDir not in sys.path:
    sys.path.insert(0, projectDir);
try:
    from Utility import mainUtil;
    from Courses.courseClass import Course;
except:
    print("Module not found");


def login():
    """
    Handles the student login functionality. The user has up to 5 attempts to log in successfully.
    On success, the user is redirected to the post-login menu.
    """
    loginAttempt = 0;  # Counter for login attempts
    enterLogin = ["<username>", "<password>"];  # Placeholder for username and password
    tryLogin = [False, loginAttempt];  # Tracks login success and attempts count
    print("Student Login");  # Display the login prompt
    filePath = os.path.join(projectDir, "Users", "Student", "StudentData", "studentLogin.csv");
    # Create and initialize the CSV file if it doesn't exist
    if not os.path.isfile(filePath):
        print("No students added yet!");
        quit();
    # Loop until login is successful or attempts exceed 5
    while tryLogin[0] == False and loginAttempt < 5:
        enterLogin[0] = input("Enter Username: ");  # Prompt for username
        enterLogin[1] = input("Enter Password: ");  # Prompt for password

        # Attempt login using mainUtil's login method
        tryLogin = mainUtil.login(os.path.join(os.getcwd(), "Users", "Student", "StudentData", "studentLogin.csv"),2,3,enterLogin,loginAttempt);
        loginAttempt = tryLogin[1];  # Update login attempt count

    print("Login Successful");  # Notify successful login
    postLogin(tryLogin[2][:3]);  # Pass the user data to post-login


def postLogin(loginUser):
    """
    Handles post-login operations, initializes the global logged-in student, and redirects to the student menu.
    """
    global loggedInUser;  # Declare global variable for the logged-in student
    loggedInUser = Student(loginUser[0], loginUser[1], loginUser[2]);
    
    # Retrieve and set the user's enrolled classes
    enrolledClasses = retrieveClasses(loggedInUser.getUsername());
    loggedInUser.setClasses(enrolledClasses);
    
    print(f"Welcome {loggedInUser.getFirstNm()}!");  # Greet the student
    studentMenu();  # Redirect to the student menu


def studentMenu():
    """
    Main menu for student actions such as viewing classes or logging out.
    """
    print("What would you like to do?");  # Prompt student for their choice
    options = ["Enroll in Classes","View Your Classes", "Logout"];  # Menu options
    selection = mainUtil.menu(options,True);  # Display menu and capture selection

    if selection == 1:
        enrollClass();

    elif selection == 2:
        viewStudentClass();
        studentMenu();
    else:
        print("Successfully logged out");  # Notify logout
        print("Login to different account?");  # Ask if they want to log in again
        options = ["Login Again"];  # Provide login option
        selection = mainUtil.menu(options, True);  # Display menu and capture selection
        if selection == 1:
            login();  # Redirect to login


def enrollClass():
    """
    Allows a user to enroll in a class.
    Displays available classes (excluding already enrolled ones) and saves the selected enrollment to a file.
    """
    username = loggedInUser.getUsername();

    # Prepare the enrollment record
    newEnrollment = [username, ""];

    # Get available classes (excluding already enrolled classes)
    availableClasses = enrollableClass();
    if not availableClasses:  # If no classes are available
        print("No Available Classes.");
        options = ["Back to Main Menu"];
    else:
        # Create list of available class numbers, adding "Back to Main Menu" option
        options = [];
        for cls in availableClasses:
            options.append(cls.courseNumber);
        options.append("Back to Main Menu");

    # Display menu and get the user's selection
    selection = mainUtil.menu(options, True);
    if selection == len(options):  # User chose "Back to Main Menu"
        studentMenu();

    # Process the selected course
    selectedCourse = availableClasses[selection - 1].courseNumber;
    newEnrollment[1] = str(selectedCourse);

    # Check if the student is already enrolled in the selected course
    #Shouldn't be possible but double check
    if selectedCourse in [cls.courseNumber for cls in loggedInUser.getClasses()]:
        print(f"You are already enrolled in course: {selectedCourse}.");
        return;  # Prevent enrollment if already enrolled

    # Save the enrollment and update the user's classes
    try:
        mainUtil.addToDataFile(newEnrollment, os.path.join(projectDir, "Courses", "courseEnroll.csv"));
        print(f"Successfully enrolled in course: {selectedCourse}");
    except:
        print("Failed to enroll due to an error");

    loggedInUser.setClasses(retrieveClasses(username));

    # Provide options to the student for the next action
    options = ["Enroll in another course", "Main Menu"];
    selection = mainUtil.menu(options, True);
    if selection == 1:
        enrollClass();
    else:
        studentMenu();


def retrieveClasses(userName):
    """
    Fetches the classes associated with the student or instructor from the course information file.
    Returns a list of Course objects.
    """
    courses = [];

    # Ensure the enrollment and course info CSV files are initialized
    mainUtil.initializeCSV(os.path.join(projectDir, "Courses"), "courseEnroll.csv", ["Student", "CourseNumber"]);
    mainUtil.initializeCSV(os.path.join(projectDir, "Courses"), "courseInfo.csv", ["CourseNumber", "CourseName", "Instructor"]);

    # Load enrollment data
    enrollData = mainUtil.csvToArray(os.path.join(projectDir, "Courses", "courseEnroll.csv"), True);
    print(f"enrollData: {enrollData}");  # Debugging: Check what data is in enrollData

    # Parse the enrollment data for the provided username
    studentsClassNum = mainUtil.parseArray(enrollData, userName, 0, 1);
    print(f"studentsClassNum: {studentsClassNum}");  # Debugging: Check what studentsClassNum contains

    # Handle the case where no matching classes are found
    if not studentsClassNum:  # Check if the result is empty or None
        print(f"No classes found for user: {userName}");
        return courses;  # Return an empty list

    # Get course data from the course info CSV file
    coursesData = mainUtil.csvToArray(os.path.join(projectDir, "Courses", "courseInfo.csv"), True);
    print(f"coursesData: {coursesData}");  # Debugging: Check what data is in coursesData

    # Create a dictionary to map course numbers to course details for faster lookup
    coursesDict = {};
    for row in coursesData:
        coursesDict[row[0]] = Course(row[0], row[1], row[2]);

    # Iterate over the unique course numbers the student is enrolled in
    for sglCls in set(studentsClassNum):  # Using set() to remove duplicates
        if sglCls in coursesDict:
            courses.append(coursesDict[sglCls]);  # Add the corresponding Course object

    return courses;


def allAvailableClasses():
    """
    Fetches all available classes from the course information file.
    Returns a list of Course objects.
    """
    courses = [];

    mainUtil.initializeCSV(os.path.join(projectDir, "Courses"), "courseInfo.csv", ["CourseNumber", "CourseName", "Instructor"]);
    coursesData = mainUtil.csvToArray(os.path.join(projectDir, "Courses", "courseInfo.csv"), True);
    for row in coursesData:
        courses.append(Course(row[0], row[1], row[2]));
    return courses;


def enrollableClass():
    """
    Returns a list of classes the student can enroll in (classes not already enrolled in).
    This function ensures that classes the student is already enrolled in are not visible.
    """
    try:
        studentClasses = loggedInUser.getClasses();  # Get the student's current classes
    except AttributeError:
        print("Error: No user is logged in or classes are not initialized.");
        studentClasses = [];  # Initialize as an empty list if no classes are available

    allClasses = allAvailableClasses();  # Fetch all available classes

    # Get the list of course numbers the student is already enrolled in
    enrolledCourseNumbers = [];
    for cls in studentClasses:
        enrolledCourseNumbers.append(cls.courseNumber);

    # Filter out the classes the student is already enrolled in by comparing course numbers
    availableClasses = [];
    for cls in allClasses:
        if cls.courseNumber not in enrolledCourseNumbers:
            availableClasses.append(cls);

    return availableClasses;


def viewStudentClass():
    """
    Gets student classes and prints them out in list.
    """
    studentClasses = loggedInUser.getClasses();  # Get the list of Course objects
    print(f"{loggedInUser.getName()}'s Courses:");  # Print instructor title and name
    for course in studentClasses:
        print(str(course));


# Start the login process
login();