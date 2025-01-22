"""
File Name: lab8ClassChkAcct

First Created: 11/13/2024
Last Updated: 11/13/2024
Author: Van Robbins
Version 0.5
"""
class Account:
    def __init__(self,an="N/A",t="N/A",bal="N/A"):
        self.accountNumber= an;
        self.type= t;
        self.balance= bal;
    def __str__(self):
        numAccounts=len(self.accountNumber);
        return f"{numAccounts}Accounts\n";
    def getAccount(s):
        return s.accountNumber;
    def getType(s):
        return s.type;
    def getBalance(s):
        return s.balance;
    def setAccount(s,newAccountNum):
        s.accountNumber=newAccountNum;
    def setType(s,newType):
        s.type=newType;
    def setBalance(s,newBalance):
        s.balance;
    def deposit(s,num):
        s.balance+=float(num);
    