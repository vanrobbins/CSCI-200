"""
File name: employee.py
Purpose: This file demonstrates classes and objects
Author: Lingma Lu
Create date: 07/15/2023
Last update date:10/25/2023
version: 1.1
"""

#define an Employee class
class Employee:
    #define properties
    firstName = "";
    lastName = "";
    age = 0;
    rank = 0;
    salary = 0;

    #define methods
    #always have a "constructor" method that will set the property values; "self" refers to the object instance, it can be any text such as "self", but must be the first parameter
    def __init__(self, fn, ln, a, r, s):
        self.firstName = fn;
        self.lastName = ln;
        self.age = a;
        self.rank = r;
        self.salary = s;

    #always define a str function so that when the object is used as a string, the output will describe the object
    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "; Age: " + str(self.age) + "; Rank: " + str(self.rank) + "; Salary: " + str(self.salary);

    #It is a good idea to have a number of setters to set or change property values
    def setFirstName(s, fn):
        s.firstName = fn;

    def setLastName(s, ln):
        s.lastName = ln;

    def setAge(s, a):
        s.age = a;

    def setRank(s, r):
        s.rank = r;

    def setSalary(s, sa):
        s.salary = sa;

    #It is a good idea to have a number of getters to retrieve property values
    def getFirstName(s):
        return s.firstName;

    def getLastName(s):
        return s.lastName;

    def getAge(s):
        return s.age;

    def getRank(s):
        return s.rank;

    def getSalary(s):
        return s.salary;


    #define other methods that apply to the object
    def getName(s):
        return s.firstName + " " + s.lastName;

    def promote(s, level):
        s.rank = s.rank + level;

#end of the Employee class definition

#create an instance of the class(object)

employeeOne = Employee("Mary","Anderson", 28, 4, 50000); #use the class name and () to create and object; the constructor is called
print(employeeOne);
#change the first name
employeeOne.setFirstName("May");
print(employeeOne);
#retrieve first name
print(employeeOne.getFirstName());
#retrieve name
print("Name is " + employeeOne.getName());

#create another instance
employeeTwo = Employee("","",0,0,0);
print(employeeTwo);
#set properties one by one
employeeTwo.setFirstName("Tom");
employeeTwo.setLastName("Walker");
employeeTwo.setAge(21);
employeeTwo.setRank(5);
employeeTwo.setSalary(52000);
print(employeeTwo);

employeeTwo.promote(2);
print(employeeTwo.getRank());

#properties can be accessed outside of the class, but it is a good idea to be manipulated inside the class through methods
employeeTwo.rank = employeeTwo.rank + 1;
print(employeeTwo.rank);