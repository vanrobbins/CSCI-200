"""
File name: employeeExecutable.py
Purpose: This file demonstrate object oriented programming using objects defined in class files
Author: Lingma Lu
Create date: 07/15/2023
Last update date:03/24/2024
version: 1.1
"""
from addressClass import Address;
from employeeClass import Employee;

#create an address object first
addressOne = Address("#123","Apt B","Main Street"); #only three arguments are provided, with the rest using the default value

#create an employee object using the address object
employeeOne = Employee("Mary","Anderson", 28, 4, 50000, addressOne); #use the class name and () to create and object; the constructor is called
print(employeeOne);
print(employeeOne.address);
print(employeeOne.getAddress());