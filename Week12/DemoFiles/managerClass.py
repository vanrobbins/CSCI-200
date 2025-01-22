"""
File name: manager.py
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


#Define a child class that inherits from the Employee class

from employeeClass import Employee;

class Manager(Employee):

    #define its own properties and inherit others from the parent class
    totalManaging = 0;
    title = "";
    trainingHours = 0.0;
    rank = ""; #overwrite the rank property in the parent class


    #no constructor thus inherit from the parent class


    #Overwrite the __str__ method in the parent class, thus can print out a string with addtional properties
    def __str__(self):
        return "Manager Name: " + self.firstName + " " + self.lastName + "; Age: " + str(self.age) + "; Total Managing: " + str(self.totalManaging )+ "; Title: " + str(self.title) + "; Rank: " + str(self.rank) + "; Salary: " + str(self.salary) + "; Address: "+ str(self.address);

    #define its own setter and inherit others from the parent class
    def setTotalManaging(s, m):
        #use a setter to ensure a field value is in a valid range
        if (m > 0 and m <= 10):
            s.totalManaging = m;

    def setTitle(s, t):
        s.title = t;

    #use a setter to ensure a field value is in a valid range
    def setTrainingHours(s, h):
        if (h > 0.0 and h <= 40.0):
            s.traingHours = h;

    #overwrite the method in the parent class
    def setRank(s, r):
        s.rank = r;

    #define its own getter and inherit others from the parent class
    def getTotalManaging(s):
        return s.totalManaging;

    def getTitle(s):
        return s.title;

    def getTrainingHours(s):
        return s.trainingHours;

    #overwrite the special method in the parent class
    def getRank(s):
        return "Manager rank is " + s.rank;

    #define its own special methods
    def passTraining(s):
        if (s.trainingHours >= 20.0):
            return True;
        else:
            return False;
