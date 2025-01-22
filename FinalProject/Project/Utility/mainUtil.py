"""
File: user_utilities.py

Description:
This script contains utility functions for managing user input, validating data, handling CSV file operations, 
and implementing a basic menu system. The functionalities include:
- Displaying and processing menus.
- Validating user input for various conditions (e.g., valid strings, unique entries).
- Reading and writing data from/to CSV files.
- Handling user login attempts with a retry mechanism.

Dependencies:
- Python Standard Library: os, sys
- Custom Modules: None (Standard libraries used)

Functions:
1. menu(options, exit) - Displays a menu with a list of options and handles user selection.
2. again() - Prompts the user to decide whether to retry an action or quit.
3. check(inputX, bottom, top) - Validates if a number input is within a specified range.
4. checkValid(inputInfo, minLength, maxLength, space, numbers, specChar) - Validates if a string input meets certain criteria.
5. checkUnique(fileDirectory, column, enteredData) - Checks if a given value already exists in the specified CSV file.
6. login(file, colUN, colPass, entered, attemptNum) - Verifies a user's login credentials against a stored CSV file.
7. initializeCSV(directory, fileName, headers) - Initializes a CSV file with headers if it does not exist.
8. csvToArray(csvFile, header) - Converts a CSV file into a 2D array (list of lists).
9. parseArray(array, target, colTarget, colOutput) - Searches through a 2D array and extracts values based on the specified column.
10. addToDataFile(data, fileOpen) - Appends new data to a CSV file.
11. printTable(head, data) - Prints data in a table format with headers.

Author:
Van Robbins

Date Created:
2024-12-3

Last Updated:
2024-12-10

Version 1.0

Notes:
- The script assumes CSV files follow a specific structure and are comma-separated.
- Error handling is in place for file reading/writing issues, and login attempts are limited to 5.
- Use the `menu()` function to interact with the script via text-based options.

"""

import os
import sys

# Add the Project directory to sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Utility Functions

def menu(options, exit):
    """
    Displays a list of menu options and handles user selection.

    Args:
        options (list): List of options to display to the user.
        exit (bool): If True, include an option to exit the program.

    Returns:
        int: The selected option number.
    """
    i = 0
    while i < len(options):  # Loop through the list of options
        print(f"{i + 1}| {options[i]}")
        i += 1
    if exit:  # If exit is True, display the Exit option
        print(f"{i + 1}| Exit")
    selection = input()  # Get user input
    selectionCheck = check(selection, 1, len(options) + 1)  # Validate the input
    if selectionCheck:  # If valid input, convert to integer and return
        selection = int(selection)
    else:
        return menu(options, exit)  # Recursive call for invalid input
    if selection == (len(options) + 1) and exit:  # Check if user chose to exit
        quit()
    else:
        return selection  # Return the selected option

def again():
    """
    Prompts the user if they want to try again.

    Returns:
        bool: True if the user wants to retry, False to quit.
    """
    goAgain = input("Would you like to try again Y/N\n")
    if goAgain.upper() == "Y":
        return True
    else:
        quit()  # If the user does not want to retry, quit the program

def check(inputX, bottom, top):
    """
    Checks if the user's input is within a specified range [bottom, top].

    Args:
        inputX (str): The user input to validate.
        bottom (int): The lower bound of the valid range.
        top (int): The upper bound of the valid range.

    Returns:
        bool: True if the input is valid, False if invalid.
    """
    tryAgain = False
    try:
        inputX = int(inputX)  # Attempt to convert the input to an integer
    except:
        tryAgain = again()  # If invalid, ask the user if they want to try again
        if tryAgain:
            return False
    if bottom <= inputX <= top:  # If input is within the valid range
        return True
    else:
        tryAgain = again()  # Ask to try again if input is out of range
        if tryAgain:
            return False

def checkValid(inputInfo, minLength, maxLength, space, numbers, specChar):
    """
    Validates if a string input meets certain criteria.

    Args:
        inputInfo (str): The input string to validate.
        minLength (int): The minimum allowed length for the input string.
        maxLength (int): The maximum allowed length for the input string.
        space (bool): Whether spaces are allowed in the input.
        numbers (bool): Whether numbers are allowed in the input.
        specChar (bool): Whether special characters are allowed in the input.

    Returns:
        bool: True if the input is valid, False if invalid.
    """
    validCharacters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if space:
        validCharacters.append(" ")
    if numbers:
        validCharacters += list("0123456789")
    if specChar:
        validCharacters += list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/")

    spaceCount = 0
    if minLength <= len(inputInfo) <= maxLength:  # Check the length of the input
        for char in inputInfo:  # Iterate over each character in the input
            if char.upper() not in validCharacters:
                print("The input must only contain valid characters.")
                if again():
                    return False
                break
            elif char == " ":
                spaceCount += 1
                if spaceCount == len(inputInfo):
                    print("The input must contain more than just spaces.")
                    if again():
                        return False
                    break
        else:
            return True  # If no breaks, the input is valid
    else:
        print(f"The name must be larger than {minLength} and smaller than {maxLength}")
        if again() == True:
            return False

def checkUnique(fileDirectory, column, enteredData):
    """
    Checks if the entered data is unique in the specified column of the CSV file.

    Args:
        fileDirectory (str): The path to the CSV file.
        column (int): The column index to check for uniqueness.
        enteredData (str): The data to check for uniqueness.

    Returns:
        bool: True if the data is unique, False if it already exists.
    """
    try:
        with open(fileDirectory, mode='r') as file:
            lines = file.readlines()
    except:
        print("The system is experiencing technical difficulties")
        quit()
    for i in lines[1:]:  # Skip the header
        allAccountInfo = i.strip().split(',')
        if allAccountInfo[column].upper() == enteredData.upper():
            return False  # Data is not unique
    return True  # Data is unique

def login(file, colUN, colPass, entered, attemptNum):
    """
    Handles the user login by checking the entered username and password against the stored data.

    Args:
        file (str): The path to the login CSV file.
        colUN (int): The column index for the username.
        colPass (int): The column index for the password.
        entered (list): The entered username and password.
        attemptNum (int): The number of login attempts made so far.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    i = 0
    try:
        loginInfo = open(file, 'r')
    except:
        print("The system is experiencing technical difficulties")
        quit()
    lines = loginInfo.readlines()
    for i in lines[1:]:  # Skip header
        allAccountInfo = i.strip().split(',')
        un, pw = allAccountInfo[colUN], allAccountInfo[colPass]
        if un.upper() == entered[0].upper() and pw == entered[1]:
            return True, attemptNum, allAccountInfo[:3]  # Return login success and account details
    attemptNum += 1
    if attemptNum < 5:
        print(f"Invalid Username or Password\n{5 - attemptNum} tries remaining")
        again()  # Ask if the user wants to try again
        return False, attemptNum
    else:
        print("No more login attempts")
        quit()

def initializeCSV(directory, fileName, headers):
    """
    Initializes a CSV file with headers if it does not exist.

    Args:
        directory (str): The directory where the CSV file is stored.
        fileName (str): The name of the CSV file.
        headers (list): The header row for the CSV file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it doesn't exist
    filePath = os.path.join(directory, fileName)
    if not os.path.isfile(filePath):
        with open(filePath, mode='w') as file:
            file.write(",".join(headers) + "\n")  # Initialize the file with headers

def csvToArray(csvFile, header):
    """
    Converts a CSV file into a 2D array (list of lists).

    Args:
        csvFile (str): Path to the CSV file.
        header (bool): Whether the CSV file contains a header row.

    Returns:
        list: A 2D array containing the CSV data, excluding the header if specified.
    """
    try:
        fileData = open(csvFile, 'r')
    except:
        print("The system is experiencing technical difficulties")
        quit()
    allData = []
    startLine = 1 if header else 0  # Skip the header line if needed
    lines = fileData.readlines()
    for line in lines[startLine:]:
        lineData = line.strip().split(',')  # Assume CSV is comma-separated
        allData.append(lineData)
    fileData.close()
    return allData

def parseArray(array, target, colTarget, colOutput):
    """
    Searches through a 2D array and extracts values based on the specified column.

    Args:
        array (list): The 2D array to search.
        target (str): The value to search for.
        colTarget (int): The column index to search in.
        colOutput (int): The column index to output data from.

    Returns:
        list: The extracted values from the specified column.
    """
    output = []
    if colTarget is not None:
        for row in array:
            if row[colTarget] == target:
                if colOutput is not None:
                    output.append(row[colOutput])
                else:
                    output.append(row)
    else:
        for row in array:
            for elmt in row:
                if elmt == target:
                    if colOutput is not None:
                        output.append(row[colOutput])
                    else:
                        output.append(row)

def addToDataFile(data, fileOpen):
    """
    Appends new data to a CSV file.

    Args:
        data (list): The data to append to the file.
        fileOpen (str): The path to the file to append data to.
    """
    i = 0
    try:
        fileData = open(fileOpen, 'a')
    except:
        print("The system is experiencing technical difficulties")
        quit()
    while i < len(data):
        oneValue = data[i]
        if i == len(data) - 1:
            fileData.write(str(oneValue) + '\n')
        else:
            fileData.write(str(oneValue) + ',')
        i += 1

def printTable(head, data):
    """
    Prints data in a table format with headers.

    Args:
        head (list): The column headers.
        data (list): The data to print.
    """
    for col in head:
        print(col.ljust(20), end="")
    print()

    for i, row in enumerate(data, start=0):  # Print table rows
        for col in row:
            print(str(col).ljust(20), end="")
        print()
