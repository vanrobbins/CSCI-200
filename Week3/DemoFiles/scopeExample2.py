"""
File Name: scopeExample2.py
Purpose:
    This file demonstrates the use of functions and local variables.
    Key concept - define one function for different currency conversions
    Pro: code simplicity, no hard coding
    Con: ???
    A US dollar value will be converted to Euro, Turkish Lira and Chinese Yuan through three function calls.
First Create Date: September 6, 2023
Last Update Date: Janauary 30, 2024
Author: Lingma Lu
Version: 1.1
"""

#create variables to store the currency value in dollars
currencyDollarValue = 10;
euroRate = 0.93;
turkishLiraRate = 26.78;
chineseYuanRate = 7.32;

#define a function to convert the dollar value to Euro
def convert(v, r):
    return v*r;


#function calls
print(str(currencyDollarValue) + " dollars converted to Euro is " + str(convert(currencyDollarValue, euroRate)));
print(str(currencyDollarValue) + " dollars converted to Turkish Lira is " + str(convert(currencyDollarValue, turkishLiraRate)));
print(str(currencyDollarValue) + " dollars converted to Chinese Yuan is " + str(convert(currencyDollarValue, chineseYuanRate)));
