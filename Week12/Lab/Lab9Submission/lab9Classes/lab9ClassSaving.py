"""
File Name: lab9ClassSaving

Defines Saving class; sub class of Account

First Created: 11/13/2024
Last Updated: 11/19/2024
Author: Van Robbins
Version 0.5
"""
from lab9Classes.lab9ClassAccount import Account;
class Saving(Account):
    def __str__(s):
        return f"Saving Account: {s.accountNumber} Balance: ${s.balance:.2f}";
    def setInterest(s,percent):#Sets interest from a percent number
        s.interest=(percent/100);
    def getInterest(s):#Returns interest as a percent
        return f"{(s.interest*100):.2f}%"
    def applyInterest(s):#Applies Interest
        s.balance*=1+(s.interest);

    
