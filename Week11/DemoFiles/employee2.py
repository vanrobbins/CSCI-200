"""
File name: employee2.py
Purpose: This file demonstrates classes and objects whose property can be an object
Author: Lingma Lu
Create date: 07/15/2023
Last update date:3/24/2024
version: 1.1
"""
#define an Address class
class Address:
    streetNumber = "";
    optional = "";
    streetName = "";
    city = "";
    state = "";
    zip = "";

    def __init__(self, sn="", op="", sa="", ct="", st="",zp="", cn="" ): #can define default values in case no arguments are provided
        self.streetNumber = sn;
        self.optional = op;
        self.streetName = sa;
        self.city = ct;
        self.state = st;
        self.zip = zp;
        self.country = cn;

    def __str__(self):
        return self.streetNumber + ", " + self.optional + ", " + self.streetName + ", " + self.city + ", " + self.state + ", " + self.zip + ", " + self.country;

#end of the Address class definition

#define an Employee class
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

#end of the Employee class definition

#create an instance of the class(object)

#create an address object first

addressOne = Address("#123","Apt B","Main Street"); #only three arguments are provided, with the rest using the default value

employeeOne = Employee("Mary","Anderson", 28, 4, 50000, addressOne); #use the class name and () to create and object; the constructor is called
print(employeeOne);
print(employeeOne.address);
print(employeeOne.getAddress());


#in class exercise:
#1. complete the getters and setters for the Address class
#2. define a method isIndiana() to determine if the address is an Indiana address, returns true of false
#use setter methods to provide the rest of the property values for the addressOne object.
#create a second employee object, provides all property values, then call the method to determine if the second employee is an Indiana resident


