"""
File Name: scopeExample3.py
Purpose:
    This file demonstrates the use of functions and global variables.
    Key concept - use a global variable to simplify the conversion algorithm. Only one function with one input parameter is needed.
    Pro: code simplcity
    Con: convert() function is not stand-alone. Must have a global variable outside of the function for it to work.
    A US dollar value will be converted to Euro, Turkish Lira and Chinese Yuan through three function calls.
First Create Date: September 6, 2023
Last Update Date: January 30, 2024
Author: Lingma Lu
Version: 1.1
"""

#create variables to store the currency value in dollars
currencyDollarValue = 10;
euroRate = 0.93;
turkishLiraRate = 26.78;
chineseYuanRate = 7.32;

#define a function to convert the dollar value to Euro
def convert(r):
    return currencyDollarValue*r; #global variable is used


#function calls
print(str(currencyDollarValue) + " dollars converted to Euro is " + str(convert(euroRate)));
print(str(currencyDollarValue) + " dollars converted to Turkish Lira is " + str(convert(turkishLiraRate)));
print(str(currencyDollarValue) + " dollars converted to Chinese Yuan is " + str(convert(chineseYuanRate)));

