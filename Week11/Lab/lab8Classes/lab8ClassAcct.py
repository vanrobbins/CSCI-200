"""
File Name: lab8ClassAcct

First Created: 11/13/2024
Last Updated: 11/13/2024
Author: Van Robbins
Version 0.5
"""

class AccountHolder:
    firstName="";
    lastName=""
    dob="";
    checking=0;
    saving=0;
    def __init__(self,arr):
        self.first= arr[0];
        self.last= arr[1];
        self.dob= arr[2];
        self.checking = arr[3];
        self.saving = arr[4];
    def __str__(self):
        return f"Name: {self.first} {self.last}\nChecking Account:{self.checking}\nSaving Account:{self.saving}";
    
    def getName(s):
        return f"{s.first} {s.last}";
    def getDOB(s):
        return f"{s.dob}"
    def getChecking(s):
        return s.checking
    def getSaving(s):
        return s.saving
    