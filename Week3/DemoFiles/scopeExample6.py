"""
File Name: scopeExample6.py
Purpose:
    This file demonstrates the use of functions and global variables.
    Key concept - add a label inside each function to be used in the print statement
    Pro: the return value is used to output the label, and the result is stored in the global variable, thus a function can pass two values out
    Con: code complexity, hard coding, functions are not stand-alone
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
    currencyName = "Euro";
    return currencyName;

#define a function to convert the dollar value to Turkish Lira
def convertTurkishLira():
    global result;
    result = currencyDollarValue*26.78;
    currencyName = "Tukish Lira";
    return currencyName;

#define a function to convert the dollar value to Chinese Yuan
def convertChineseYuan():
    global result;
    result = currencyDollarValue*7.32;
    currencyName = "Chinese Yuan";
    return currencyName;


#function calls

print(str(currencyDollarValue) + " dollars converted to " + convertEuro() + " is " + str(result));

print(str(currencyDollarValue) + " dollars converted to " + convertTurkishLira() + " is " + str(result));

print(str(currencyDollarValue) + " dollars converted to " + convertChineseYuan() + " is " + str(result));

