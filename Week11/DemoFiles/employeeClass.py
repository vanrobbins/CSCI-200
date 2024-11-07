"""
File name: employeeClass.py
Purpose: This file defines the Address class
Author: Lingma Lu
Create date: 10/25/2023
Last update date:10/25/2023
version: 1.1
"""

from addressClass import Address;

class Employee:
    #define properties
    firstName = "";
    lastName = "";
    age = 0;
    rank = 0;
    salary = 0;
    address = Address();


    #define methods
    #always have a "constructor" method that will set the property values; "self" refers to the object instance, it can be any text value, but must be the first parameter
    def __init__(self, fn, ln, a, r, s, ad):
        self.firstName = fn;
        self.lastName = ln;
        self.age = a;
        self.rank = r;
        self.salary = s;
        self.address = ad;

    #always define a str function so that when the object is used as a string, the output will describe the object
    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "; Age: " + str(self.age) + "; Rank: " + str(self.rank) + "; Salary: " + str(self.salary) + "; Address: "+ str(self.address);

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

    def getAddress(self):
         return self.address.streetNumber + ", " + self.address.optional + ", " + self.address.streetName + ", " + self.address.city + ", " + self.address.state + ", " + self.address.zip + ", " + self.address.country;

    def promote(s, level):
        s.rank = s.rank + level;
