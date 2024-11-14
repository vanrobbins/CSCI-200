"""
File Name: lab8ClassChkAcct

First Created: 11/13/2024
Last Updated: 11/13/2024
Author: Van Robbins
Version 0.5
"""
class Checking:
    accountNumber=0;
    pin="";
    balance=0;
    def __init__(self,arr):
        self.accountNumber= int(arr[0]);
        self.pin= arr[1];
        self.balance= float(arr[2]);
    def __str__(self):
        return f"Account:{self.accountNumber}\nBalance:{self.balance}";
    
    def getAccountNumber(s):
        return s.accountNumber;
    def getPin(s):
        return s.pin;
    def deposit(s,num):
        s.balance+=num;
    def deposit(s,num):
        s.balance+=float(num);
    def withdraw(s,num):
        if float(num)<=s.balance:
            s.balance-=float(num);
        else:
            print("Not enough money to withdraw")