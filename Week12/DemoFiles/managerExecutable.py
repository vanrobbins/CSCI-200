"""
File name: managerExecutable.py
Purpose: This file demonstrates object inheritance
Author: Lingma Lu
Create date: 07/15/2023
Last update date:4/1/2024
version: 1.1
"""

"""
Inheritance allows us to define a class that inherits some or all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
A child class can define its own constructor.
A child class can define a property or method of the same name as in the parent class.
If a property or method is referenced on an object, the program will first look for the definition in the child class; if not found, will look for it in the parent class.
"""

from addressClass import Address;
from managerClass import Manager;

addressOne = Address("#123","Apt B","Main Street", "Indianapolis", "IN", "46202", "USA");

#create a Manager object using the address object
managerOne = Manager("Mary","Anderson", 28, 4, 50000, addressOne); #parent class (Employee) constructor is called, since none is defined in the Manager class

#this will print out all the property values inherited from the parent class and the initial property values from the Manager class
print(managerOne); #its own __str__ method is called, "method overwrite" happened

#set values for its own properties
managerOne.setTotalManaging(100); #this line will not take effect because of the validation inside the method
managerOne.setTitle("Floor Superviser");
managerOne.setRank("Full Time L2");
managerOne.setTrainingHours(15);

#print out all the property values again
print(managerOne);

#a method in its own class is called, even if it exists in the parent class
print(managerOne.getRank());

#a method in the child class is called
print(managerOne.passTraining());
