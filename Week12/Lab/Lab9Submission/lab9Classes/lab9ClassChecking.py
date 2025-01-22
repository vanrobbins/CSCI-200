"""
File Name: lab8ClassChecking

Defines Checking class; sub class of Account

First Created: 11/13/2024
Last Updated: 11/19/2024
Author: Van Robbins
Version 0.5
"""
from lab9Classes.lab9ClassAccount import Account;
class Checking(Account):
    pin=None;#Defines pin if not yet defined
    def __str__(s):
        return f"Checking Account: {s.accountNumber} Balance: ${s.balance:.2f}";
    def setPin(s,p):
        if s.pin==None:#Account does not have pin merely add it to class
            s.pin=p;
        else:#Account already has a pin; must know current pin to change pin
            oldPin=input("Input current Pin: ");
            if oldPin==s.pin:
                newPin=input("Input new Pin: ");
                s.pin= newPin;
    def getPin(s):
        return s.pin;