"""
File Name: lab5
Purpose:
Can add employee to database
Searches Database for employee Info
Your program will process a long string with a fixed structure, whose parts are separated using specific characters. 

The program will search through the string, and perform at least two types of operations - 
one about string operations such as searching for something or encrypting a text
another about performing mathematical computations such as finding the average, total, or largest value etc. 


Special Requirements: 
+ 20 points if the initial string is formed through user inputs. Each piece of information is taken from the user input (10’) and there are robust input validations(10’).
You can use any Python built-in string methods except split(), rsplit() and splitlines(). https://www.w3schools.com/python/python_ref_string.asp
-20 points if any of the three methods is used.

First Created: 9/28/2024
Last Updated: 10/1/2024
Author: Van Robbins
Version 1.1
"""
#Imports Utility File
import lab5Utility;
import math;
#Asks User if wants to add an employee to data or search for employee
def mainMenu(first):
    #If first time running adds introduction and does not provide option to exit
    if first==True:
        print("Walcome to Van's Employee Database\nYou can create, look up, or learn about the employees in the database")
        findOrCreate=input("Would you like to\n1| Create\n2| Look Up\n3| About Data\n");
        checkInput= lab5Utility.check(findOrCreate,1,3); #Ensures Input is valid, 1 or 2
    else:
        findOrCreate=input("Would You Like To\n1| Create\n2| Look Up\n3| About Data\n4| Exit\n");
        checkInput= lab5Utility.check(findOrCreate,1,4);
    if checkInput==True: #If input is valid convert to int and send to function based on input
            validInput=int(findOrCreate);
            if validInput==1:
                create();#Go to create 
            elif validInput==2:
                look();
            elif validInput==3:
                about();
            else:
                exit();
    else:#Input is invalid, if user opted to try again will do so
        if checkInput=="goAgain":
            mainMenu(False);
        else:
            quit();
    
#Asks user questions to add employee to database
def create():
    dataAdd=open("dataLab5.txt","a+");#Opens text file in mode to append data

    print("\nLet's create this employees profile!")
    firstName=input("What is the employee's first name?\n");
    #Checks that Input is 35 Characters or less
    checkFirstNm= lab5Utility.checkInputLength(firstName,35);
    while checkFirstNm!=True:
        if checkFirstNm=="goAgain":
            firstName=input("What is the employee's first name?\n");
            checkFirstNm= lab5Utility.checkInputLength(firstName,35);
        else:
            quit();
    #LAST NAME
    lastName=input("What is the employee's last name?\n");
    #Checks that Input is 35 Characters or less
    checklastNm=lab5Utility.checkInputLength(lastName,35);
    while checklastNm!=True:
        if checklastNm=="goAgain":
            lastName=input("What is the employee's last name?\n");
            checklastNm=lab5Utility.checkInputLength(lastName,35);
        else:
            quit();
    #AGE
    age=input(f"How old is {firstName} {lastName}?\n");
    #Checks that age is between 16 and 120
    checkAge= lab5Utility.check(age,16,120);
    while checkAge!=True:
        if checkAge=="goAgain":
            age=input(f"How old is {firstName} {lastName}?\n");
            checkAge= lab5Utility.check(age,16,120);
        else:
            quit();
    #TITLE
    title=input(f"What is {firstName} {lastName}'s title?\n");
    #Checks that Input is 35 Characters or less
    checkTitle=lab5Utility.checkInputLength(title,35);
    while checkTitle!=True:
        if checkTitle=="goAgain":
            title=input(f"What is {firstName} {lastName}'s title?\n");
            checkTitle=lab5Utility.checkInputLength(title,35);
        else:
            quit();
    #SALARY
    salary=input(f"What is {firstName} {lastName}'s yearly salary\n");
    #Checks that Input is greater than 0
    checkSalary= lab5Utility.checkPositiveNonZero(salary);
    while checkSalary!=True:
        if checkSalary=="goAgain":
            salary=input(f"What is {firstName} {lastName}'s yearly salary\n");
            checkSalary= lab5Utility.checkPositiveNonZero(salary);
        else:
            quit();
    #ADDS ALL OF EMPLOYEE INFO TO END OF FILE
    dataAdd.write(f"{firstName}|{lastName}|{age}|{title}|{salary};");
    dataAdd.close();#CLOSES FILE ENSURING DATA IS SAVED
    print("\n\n---------------------------")
    print("Employee Successfully Added");
    print("---------------------------")
    mainMenu(False);

    
#Looks for employee, ALL EMPLOYEES MUST HAVE UNIQUE NAME
def look():
    dataSearch = open("dataLab5.txt","r+"); #Opens data text file in read only mode
    lowerData=dataSearch.read();#Sets current database to data string

    print("\nLet's look for this employee!")
    firstName=input("First Name:\n");#Asks user to insert first name of employee they are looking for
    lastName=input("Last Name:\n");#Asks user to insert last name of employee they are looking for
    #Do not need to ensure entry is valid as all entries in database were validated at entry

    #Search using uppercase so doesn't matter user inputs capitalization
    firstLastName=(firstName+"|"+lastName).upper();#Combines first and last name into an uppercase string divided by | like in data
    upperData=lowerData.upper()#Makes a version of the entire data in uppercase for searching purposes

    #EMPLOYEE IS IN DATABASE
    if(firstLastName in upperData):
        print("\n\nEmployee Found\n--------------");
        
        startIndex=upperData.find(firstLastName);#Finds Index where first and last name is in uppercase data
        employeeInfo=lab5Utility.cut(lowerData,startIndex, ";","|");#Cuts data into parts given the regular data, the start of the data wanted, the end character, and divider character
        print(f"{employeeInfo[0]} {employeeInfo[1]}\nAge: {employeeInfo[2]}\nRole: {employeeInfo[3]}\nSalary: {employeeInfo[4]}");#Prints each part
        print("--------------\n");
        
    
    #EMPLOYEE WAS NOT FOUND
    else:
        print("\nEmployee Not Found\n")
    dataSearch.close();#Closes text file

    #SENDS USER BACK TO MAIN MENU FUNCTION False becauase not first time running
    mainMenu(False);

def about():
    dataSearch = open("dataLab5.txt","r+");#Opens text file in mode to read data
    #SEES HOW MANY ENTRIES ARE IN THE DATABASE
    currentNumberEntries=lab5Utility.amountEntry(dataSearch.read(),";");
    dataSearch.close();#CLOSES text file
    averageSalary=round(findAverageSalary(int(currentNumberEntries)),2);
    print("\n\n---------------------------")
    print(f"About the Data:\nThere's {currentNumberEntries} employees in the system!");
    print(f"The average salary is ${averageSalary}")
    print("---------------------------")
    mainMenu(False);

def findAverageSalary(entries):
    dataSearch = open("dataLab5.txt","r+");#Opens text file in mode to read data
    allData=dataSearch.read();
    index=0;
    totalSum=0
    while index!=len(allData):
        if(allData[index])=="|":#If the character at the index of the data is the same as the divider append that part to array
            start=index+1; #For next data part the start will be at the end of the last part
            index+=1;
        elif((allData[index])==";"):
            personSalary=int(allData[start:index]);
            totalSum=totalSum+personSalary;
            index+=1;
        else: #Character is neither divider or end
            index+=1;
    average=totalSum/entries;
    dataSearch.close();#Closes text file
    return average

    
#RUNS Initial main menu, True since first time running
mainMenu(True);