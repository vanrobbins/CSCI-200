"""
File Name: lab8OOPBankingUtility

First Created: 11/13/2024
Last Updated: 11/13/2024
Author: Van Robbins
Version 0.5
"""
import datetime;
currentTime=datetime.datetime.now();
currentYear=currentTime.year;
currentMonth=currentTime.month;
currentDay=currentTime.day;

def check(inputX, bottom, top):
    tryAgain=False;
    try:
       inputX=int(inputX);
    except:
        tryAgain=again();
        if tryAgain==True:
            return False;
    if inputX>=bottom and inputX<=top:
        return True;
    else:
        tryAgain=again();
        if tryAgain==True:
            return False;        
        
def again():
    goAgain=input("Would you like to try again Y/N\n");
    if goAgain.upper()=="Y":
        return True;
    else:
        quit();

def nameDOB(minAge,maxAge,maxNameLength):
    firstName=input("Enter First Name: ");
    checkFirst=checkName(firstName,maxNameLength);
    if checkFirst==False:
        firstName=input("Enter First Name: ");
        checkFirst=checkName(firstName,maxNameLength);
    lastName=input("Enter Last Name: ");
    checkLast=checkName(lastName,maxNameLength);
    if checkLast==False:
        lastName=input("Enter Last Name: ");
        checkLast=checkName(lastName,maxNameLength);
    print("Enter Date of Birth")
    dateOfBirth=createDate(minAge,maxAge);
    return[firstName,lastName,dateOfBirth]

def checkName(inputName, maxlength):
    validCharacters= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '];
    if len(inputName)<=maxlength:
        for i in range(len(inputName)):
            if inputName[i].upper() not in validCharacters:
                print(f"The input must only contain letters of the alphabet");
                if again()==True:
                    return False;
                break;
            elif i==len(inputName)-1:
                return True;
    else:
        print(f"The name must be smaller than {maxlength}");
        if again()==True:
            return False;

def createDate(minAge,maxAge):
    validYears=[currentYear-maxAge,currentYear-minAge]
    yearInput=year(validYears[0],validYears[1]);
    if yearInput==False:
        yearInput=year(validYears[0],validYears[1]);
    leapyear=checkLeapYear(yearInput);
    monthsDays=createDateTable(leapyear);
    monthInput=month(yearInput,validYears[0],validYears[1]);
    if monthInput==False:
        monthInput=month(yearInput,validYears[0],validYears[1]);
    dayInput=day(yearInput,validYears[0],validYears[1],monthInput,monthsDays);
    if dayInput==False:
        dayInput=day(yearInput,validYears[0],validYears[1],monthInput,monthsDays);
    return f"{monthInput}/{dayInput}/{yearInput}"

def year(minYear,maxYear):
    checkYear=0;
    yearEntered=input("Enter Year: ")
    checkYear=check(yearEntered,minYear,maxYear);
    if checkYear==True:
        return int(yearEntered);
    else:
        return False
    
def month(year,minYear,maxYear):
    monthEntered=input("Enter Month: ");
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
    checkMonth=check(monthEntered,monthMin,monthMax);
    if checkMonth==True:
        return int(monthEntered);
    else:
        return False

def day(year,minYear,maxYear,month,dateTable):
    dayEntered=input("Enter Day: ")
    if year==maxYear and month==currentMonth:
        checkDay=check(dayEntered,1,currentDay);
    elif year==minYear and month==currentMonth:
        checkDay=check(dayEntered,currentDay,dateTable[month-1]);
    else:
        checkDay=check(dayEntered,1,dateTable[month-1]);
    if checkDay==True:
        return int(dayEntered);
    else:
        return False

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

def addDataFile(data,currentDirectory,fileOpen):
    i=0;
    try:
        fileData=open(currentDirectory+fileOpen, 'a');
    except:
        #If cannot quit
        print("The system is experiencing technical difficulties");
        quit();
    while (i<len(data)):
        oneValue = data[i];
        #If at end of row write last value and median or median header
        if (i ==(len(data)-1)):
            fileData.write(str(oneValue)+'\n');
        else:
            fileData.write(str(oneValue)+',');
        i+=1;