"""
File name: addressClass.py
Purpose: This file defines an Address class
Author: Lingma Lu
Create date: 07/15/2023
Last update date:10/31/2023
version: 1.1
"""

"""
Inheritance allows us to define a class that inherits some of all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
A child class can define its own constructor.
A child class can define a property of method of the same name as in the parent class.
If a property or method is referenced on an object, the program will first look for the definition in the child class; if not found, will look for it in the parent class.
"""

#define a NewAddress class
class Address:
    streetNumber = "";
    optional = "";
    streetName = "";
    city = "";
    state = "";
    zip = "";

    def __init__(self, sn="N/A", op="N/A", sa="N/A", ct="N/A", st="N/A",zp="N/A", cn="N/A" ): #can define default values in case no arguments are provided
        self.streetNumber = sn;
        self.optional = op;
        self.streetName = sa;
        self.city = ct;
        self.state = st;
        self.zip = zp;
        self.country = cn;

    def __str__(self):
        return self.streetNumber + ", " + self.optional + ", " + self.streetName + ", " + self.city + ", " + self.state + ", " + self.zip + ", " + self.country;

#end of the NewAddress class definition
