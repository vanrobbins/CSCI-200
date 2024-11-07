"""
File Name: lab6Utility
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
import datetime;
currentTime=datetime.datetime.now();
currentYear=currentTime.year;
currentMonth=currentTime.month;
currentDay=currentTime.day;

def check(userInput,bottom,top):
    validSize=[];
    current=bottom;
    while current<=top:
        validSize.append(str(current));
        current+=1;
    if userInput not in validSize:
        print(f"The input must be between {bottom} and {top}");
        again=input("Would you like to try again Y/N\n");
        if(again.upper()=="Y"):
            return "again";
        else:
            return False;
    else:
        return int(userInput);


def createDate(minAge,maxAge):
    validYears=[currentYear-maxAge,currentYear-minAge]
    yearInput=year(validYears[0],validYears[1]);
    if yearInput=="again":
        yearInput=year(validYears[0],validYears[1]);
    elif yearInput==False:
        quit();
    leapyear=checkLeapYear(yearInput);
    monthsDays=createDateTable(leapyear);
    monthInput=month(yearInput,validYears[0],validYears[1]);
    if monthInput=="again":
        monthInput=month(yearInput,validYears[0],validYears[1]);
    elif monthInput==False:
        quit();
    dayInput=day(yearInput,validYears[0],validYears[1],monthInput,monthsDays);
    if dayInput=="again":
        dayInput=day(yearInput,validYears[0],validYears[1],monthInput,monthsDays);
    elif dayInput==False:
        quit();
    return [monthInput,dayInput,yearInput]


def year(minYear,maxYear):
    checkYear=0;
    yearInput=input("Enter Year:\n")
    checkYear=check(yearInput,minYear,maxYear);
    return checkYear;

def month(year,minYear,maxYear):
    monthInput=input("Enter Month:\n");
    checkMonth=0;
    if year==maxYear:
        monthMin=1;
        monthMax=currentMonth;
    elif year==minYear:
        monthMin=currentMonth;
        monthMax=12;
    else:
        monthMin=1
        monthMax=12
    checkMonth=check(monthInput,monthMin,monthMax);
    return checkMonth;

def day(year,minYear,maxYear,month,dateTable):
    dayInput=input("Enter Day:\n")
    if year==maxYear and month==currentMonth:
        checkDay=check(dayInput,1,currentDay);
    elif year==minYear and month==currentMonth:
        checkDay=check(dayInput,currentDay,dateTable[month-1]);
    else:
        checkDay=check(dayInput,1,dateTable[month-1]);
    return checkDay;

def createDateTable(leap):
    monthDays=[];
    i=0;
    while i<12:
        if i==1:
            if leap!=True:
                days=28;
            else:
                days=29;
        elif i%2==0:
            days=31;
        else:
            days=30;
        monthDays.append(days);
        i+=1;
    return monthDays;

def checkLeapYear(year):
    if year%100==0:
        if year%400==0:
            return True;
    elif year%4==0:
        return True;
    else:
        return False;

def searchByName(first,last,arrayData):
    i=0;
    j=0;
    for i in range(len(arrayData)):
        person=arrayData[i];
        for j in range(len(person)):
            if type(arrayData[i][j])==str:
                if first.upper()==arrayData[i][j].upper() and last.upper()==arrayData[i][j+1].upper():
                    return arrayData[i]
    else:
        return False;

def checkDate(info,divider):
    if divider in info:
        return True;
    else:
        return False;

def convertAge(date,divider):
    i=0;
    dateArray=[];
    dateIntArray=[];
    dateArray=date.split(divider);

    for i in range(len(dateArray)):
        dateIntArray.append(int(dateArray[i]));
    if currentMonth>dateIntArray[0]:
        age=currentYear-dateIntArray[2]
    elif currentMonth<dateIntArray[0]:
        age=(currentYear-dateIntArray[2])-1
    else:
        if currentDay>=dateIntArray[1]:
            age=currentYear-dateIntArray[2];
        else:
            age=(currentYear-dateIntArray[2])-1
    return age;

def avgAge(arrayNumbers):
    i=0;
    total=0;
    numberAmount=len(arrayNumbers);
    for i in range(len(arrayNumbers)):
        total+=arrayNumbers[i];
    return total/numberAmount;

def checkName(inputName, maxlength):
    validCharacters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '];
    if len(inputName)<=maxlength:
        for i in range(len(inputName)):
            if inputName[i].upper() not in validCharacters:
                print(f"The input must only contain letters of the alphabet");
                again=input("Would you like to try again Y/N\n");
                break;
            elif i==len(inputName)-1:
                return True;
    else:
        print(f"The name must be between smaller than {maxlength}");
        again=input("Would you like to try again Y/N\n");
    if(again.upper()=="Y"):
        return "again";
    else:
        return False;

def printTable(head,data):
    for col in head:
        print(col.ljust(20), end="");
    print();

    # Print table rows
    for i, row in enumerate(data, start = 0):             
        for col in row:
            print(str(col).ljust(20), end = "");
        print();


