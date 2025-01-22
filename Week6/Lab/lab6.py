"""
File Name: lab6
Purpose:
Ask user to input employee information
Find Employee Age given date of birth and create new array
Allows user to search through all data and find employees average age

Get user input and create a 2-D array with at least 5 rows and 3 columns of data, 
then create a new array whose values are copied from the first array, 
plus a new column whose values are generated based on data in the first array

Special Requirements: 
You will use an array to store all the information, 
then use a loop to copy all the information from the first array to the second array, 
at the same time, 
compute the age based on the date of birth, 
and store the age information into the fourth column of the second array.
The new column values must be generated using a user-defined function.

First Created: 9/28/2024
Last Updated: 10/8/2024
Author: Van Robbins
Version 1.1
"""
import lab6Utility
import tabulate

employees=[];
def mainMenu():
    if len(employees)<5:
        print(f"There must be {5-len(employees)} in the database");
        addEmployee();
    else:
        print(f"There are {len(employees)} in the data base\n1|Add employee\n2|Search Data\n3|Quit")
        addOrSearch=input();
        checkAddOrSearch=lab6Utility.check(addOrSearch,1,3);
        if checkAddOrSearch==1:
            addEmployee();
        elif checkAddOrSearch==2:
            updatedEmployees=employeesWAge();
            print(updatedEmployees);
            searchEmployee(updatedEmployees);
        elif checkAddOrSearch==3:
            quit();
        else:
            if checkAddOrSearch=="Again":
                mainMenu();
            else:
                quit();

def addEmployee():
    newEmployee=[];
    firstName=input("First Name:\n");
    checkFirstNm=lab6Utility.checkName(firstName,35);
    if checkFirstNm!=True:
        if checkFirstNm=="again":
            addEmployee();
        else:
            quit();
    lastName=input("Last Name:\n")
    checkLastNm=lab6Utility.checkName(lastName,35);
    if checkLastNm!=True:
        if checkLastNm=="again":
            addEmployee();
        else:
            quit();
    dateOfBirth=lab6Utility.createDate(16,120);
    newEmployee.append(firstName);
    newEmployee.append(lastName);
    newEmployee.append(str(dateOfBirth[0])+"/"+str(dateOfBirth[1])+"/"+str(dateOfBirth[2]));
    employees.append(newEmployee);
    mainMenu();
#Create new array with the employees info and add age to each employees data
def employeesWAge():
    i=0;
    j=0;
    newEmployeeData=[];
    for i in range(len(employees)):
        singleEmployeeInfo=len(employees[i]);
        newEmployee=[];
        for j in range(singleEmployeeInfo):
            if lab6Utility.checkDate(employees[i][j],"/")==True:
                newEmployee.append(employees[i][j]);
                newEmployee.append(lab6Utility.convertAge(employees[i][j],"/"));
            else:
                newEmployee.append(employees[i][j]);
        newEmployeeData.append(newEmployee);
    return newEmployeeData;

#Search through employees
def searchEmployee(allEmployees):
    print("1|Search For Employee\n2|See All Employees\n3|See Average Age of employees\n4|Back to Main Menu")
    search=input();
    checkSearch=lab6Utility.check(search,1,4);
    header = ['First Name', 'Last Name', 'Date of Birth', 'Age']
    if checkSearch==1:
        first=input("First Name:\n");
        last=input("Last Name:\n");
        searchEmployee=lab6Utility.searchByName(first,last,allEmployees);
        if searchEmployee!=False:
            lab6Utility.printTable(header,[searchEmployee])
            mainMenu();
        else:
            print("Employee Not Found")
            mainMenu();
    # Print all employees info 
    elif checkSearch==2:
        lab6Utility.printTable(header,allEmployees)
        mainMenu();
    ## Average Age of employees
    elif checkSearch==3:
        employeeAges=[];
        for i in range(len(allEmployees)):
            for j in range(len(allEmployees[i])):
                if type(allEmployees[i][j])==int:
                    employeeAges.append(allEmployees[i][j]);
        averageAge=lab6Utility.avgAge(employeeAges);
        print(f"The average age of the employees is: {averageAge}\n");
        mainMenu();
    #Back to main menu
    elif checkSearch==4:
        mainMenu();
    else:
        if checkSearch=="Again":
            searchEmployee(allEmployees);
        else:
            quit();
print("Welcome to the Employee Database:\n Plese Insert 5 Employees Data\n ")
mainMenu();