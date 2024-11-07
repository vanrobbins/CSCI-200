# Lab 5 Pseudocode

## Van Robbins 10/4/2024

### Executable File

import lab6Utility
import datetime
employees=[];
def mainMenu():
    if len(employees) less than 5:
        Tell users the data needs to add 5-len(employees);
        run addEmployee() function;
    asks user what they want to do now 1|Add employee 2|Search Data 3|Quit
        addOrSearch=input();
        checkAddOrSearch=lab6Utility.check(addOrSearch,1,3);
        if checkAddOrSearch==1:
            run addEmployee() function;
        elif checkAddOrSearch==2:
            updatedEmployees=employeesWAge() function that creates new array;
            run searchEmployee(updatedEmployees) function;
        elif checkAddOrSearch==3:
            quit();
        else entry is invalid
            checkAddOrSearch will ask user if they want to try again="Again"
                mainMenu();
            else:
                quit();
def addEmployee()
    create empty array that will hold new employees data
    Asks user for first name
        check that name is valid
    Asks user for last name
        check that name is valid
    Asks user for date of birth by:
        dateOfBirth=lab6Utility.createDate(16,120) function will ensure that valid date is entered and has correct formatting
    newEmployee.append(firstName);
    newEmployee.append(lastName);
    newEmployee.append(str(dateOfBirth[0]),"/",str(dateOfBirth[1]),"/",str(dateOfBirth[2]));
    employees.append(newEmployee);
def employeesWAge():
    i=0;
    j=0;
    create empty array newEmployeeData[];
    for i in employees:
        singleEmployeeInfo=len(employees[i]);
        for j in singleEmployeeInfo:
            if lab6Utility.checkDate(employees[i][j],"/")==True checks each data entry to see if its date
                newEmployeeData[i][j]=(employees[i][j]); Add date to array
                newEmployeeData[i][j+1]=(lab6Utility.convertAge(newEmployeeData[i][j]))
            else:
                newEmployeeData[i][j]=(employees[i][j]); Add info to array
    return newEmployeeData[];
def searchEmployee(allEmployees):
    asks user what they want to do 1|Search For Employee 2|See All Employees 3|See Average Age of employees 4|Back to Main Menu
    checkSearch=lab6Utility.check(addOrSearch,1,3);
        if checkSearch==1:
            ask for first and last name in seperate inputs
            searchEmployee=lab6Utility.search(first,last,allEmployees);
            if search doesn't equal false it will return all that employees info
                print employee info in chart form;
            else:
                print employee not found
                searchEmployee(allEmployees);
        elif checkSearch==2:
            print allEmployees in chart form
        elif checkSearch==3:
            create new array employeeAges that will only contain ages;
                for i in allEmployees:
                    singleEmployeeInfo=len(employees[i]);
                    for j in singleEmployeeInfo:
                    if type(allEmployees[i][j])==Int checks each data entry to see if its date
                        newEmployeeData[i][j].append(employeeAges); Add age to array
            averageAge=lab6Utility.avgAge(employeeAges[]);
            print average age of Employees
        elif checkSearch==4:
            mainMenu();
        else entry is invalid
            checkAddOrSearch will ask user if they want to try again="Again"
                searchEmployee(allEmployees);
            else:
                quit();

### Utility File

import function that allows us to see current date and time

def check(userInput,bottom,top){
    validSize=[];
    current=bottom;
    while current<=top:
        creates array with all possible valid inputs
        validSize.append(str(current));
        current+=1;
    If input not in array:
        print(f"The input must be between {bottom} and {top}");
        again=input("Would you like to try again Y/N\n");
        if(again.upper()=="Y"):
            return "again";
        else:
            return False;
    else:
        return int(userInput);
}

def createDate(minAge,maxAge){
    get todays date with datetime
    find valid input for year month and day given todays date
    validYears=[currentYear-minAge,currentYear-minAge]
    validYearInput=year(validYear,validYears[0],validYears[1]);
    leapyear=checkLeapYear(validYearInput);
    monthsDays=createDateTable(leapyear);
    validMonthInput=month(validYearInput,validYears[0],validYears[1],currentMonth,);
    validDayInput=day(validYearInput,validYears[0],validYears[1],currentMonth,validMonthInput,monthsDays)
    return [validMonthInput,validDayInput,validYearInput]
}

def year(minYear,maxYear):
    yearInput=input("Enter Year")
    checkYear=check(year,minYear,maxYear);
    if type(checkYear)==Int:
        return checkYear;
    else entry is invalid
        if checkYear="again"
            year(minYear,maxYear);
        else:
            quit();
    return checkYear;

def month(year, minYear,maxYear,nowMonth):
    monthInput=input("Enter Month:");
        if year==maxYear:
            monthMin=1;
            monthMax=nowMonth;
        elif year==minYear:
            monthMin=nowMonth;
            monthMax=12;
        else:
            monthMin=1
            monthMax=12
        checkMonth=check(monthInput,monthMin,monthMax);
        if type(checkMonth)==Int:
            return checkMonth;
        else entry is invalid
            if checkYear="again"
                month(year, minYear,maxYear,nowMonth);
            else:
                quit();

def day(year,minYear,maxYear,month,nowMonth,dateTable):
    dayInput=input("Enter Day:")
    if year==maxYear and month==nowMonth:
        checkDay=check(dayInput,1,currentDay);
    elif checkYear==validYear[1] and month==currentMonth:
        checkDay=check(dayInput,currentDay,monthsDays[month-1]);
    else:
        checkDay=check(dayInput,1,monthsDays[month-1]);
    if type(checkDay)==Int:
        return checkDay;
    else day entry is invalid
        if checkDay="again":
            day(year,minYear,maxYear,month,nowMonth,dateTable)
        else:
            quit();

def createDateTable(leap):
    monthDays=[];
    i=0;
    j=0;
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

def checkLeapYear(year){
    i=0;
    brokenTotal=0;
    for i in len(year){
        brokentotal+=year[i];
    }
    if brokenTotal%4==0:
        return True;
    else:
        return False;

}

def searchByName(first,last,arrayData){
    i=0;
    j=0;
    for i in arrayData:
        person=arrayData[i];
        for j in person:
            if first==arrayData[i][j] and last==arrayData[i][j+1]:
                return arrayData[i]
    else:
        return False;
}
def checkDate(info,divider){
    if divider in info:
        return True;
    else:
        return False;
}
def convertDateToAge(date,divider):
    i=0;
    dateArray=[];
    use current date to find age
    dateArray=date.split(divider)
    for i in dateArray:
        dateArray[i]=int(dateArray[i]);
    if currentMonth>dateArray[0]:
        age=dateArray[2]-currentYear
    elif currentMonth<dateArray[0]:
        age=(dateArray[2]-currentYear)-1
    else:
        if currentDay>=dateArray[1]:
            age=dateArray[2]-currentYear
        else:
            age=(dateArray[2]-currentYear)-1
    return age;

def avgAge(arrayNumbers):
    i=0;
    total=0;
    numberAmount=len(arrayNumbers);
    for i in arrayNumbers:
        total+=arrayNumbers[i];
    return total/numberAmount;
