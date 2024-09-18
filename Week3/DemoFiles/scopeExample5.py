"""
File Name: scopeExample5.py
Purpose:
    This file demonstrates the use of functions and global variables.
    Key concept - use only global variables, but one global variable's value is changed inside functions.
    Pro: ???
    Con: no code simplicity, hard coding, functions are not stand-alone
    A US dollar value will be converted to Euro, Turkish Lira and Chinese Yuan through three function calls.
First Create Date: September 6, 2023
Last Update Date: January 30, 2024
Author: Lingma Lu
Version: 1.1
"""

#create variables to store the currency value in dollars
currencyDollarValue = 10;
result = 0;

#define a function to convert the dollar value to Euro
def convertEuro():
    global result;
    result = currencyDollarValue*0.93;

#define a function to convert the dollar value to Turkish Lira
def convertTurkishLira():
    global result;
    result = currencyDollarValue*26.78;

#define a function to convert the dollar value to Chinese Yuan
def convertChineseYuan():
    global result;
    result = currencyDollarValue*7.32;


#function calls
convertEuro();
print(str(currencyDollarValue) + " dollars converted to Euro is " + str(result));

convertTurkishLira();
print(str(currencyDollarValue) + " dollars converted to Turkish Lira is " + str(result));

convertChineseYuan();
print(str(currencyDollarValue) + " dollars converted to Chinese Yuan is " + str(result));

