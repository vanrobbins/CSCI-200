"""
File Name: lab8ClassAccountHolder
Defines Account Holder Information and their related Account Classes

First Created: 11/13/2024
Last Updated: 11/19/2024
Author: Van Robbins
Version 0.5
"""
class AccountHolder:
    def __init__(self,fn,ln,dob,ad):
        self.first= fn;
        self.last= ln;
        self.dob= dob;
        self.account=ad;#Should be account class or account subclass
            
    def __str__(s):
        accountStr = "\n".join(str(acc) for acc in s.account) #Combines all account information into string
        return f"{s.first} {s.last}\nAccounts:\n{accountStr}";
    #SETTERS AND GETTERS
    def getFirstNm(s):
        return s.first;
    def getLastNm(s):
        return s.last;
    def getName(s):
        return f"{s.first} {s.last}";
    def getDOB(s):
        return f"{s.dob}"
    def getAccount(s):
        return s.account;
    def setFirstNm(s, newFirst):
        s.first=newFirst;
    def setLastNm(s, newLast):
        s.last=newLast;
    def setDOB(s, newDOB):
        s.dob=newDOB;
    def setAccount(s,AccountObject):
        s.account.append(AccountObject);#MUST BE ACCOUNT OBJECT BEING ADDED TO ACCOUNT ARRAY

    