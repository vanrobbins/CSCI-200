"""
File Name: scopeExample4.py
Purpose:
    This file demonstrates the use of functions and global variables.
    Key concept - use only global variable. No local variables are ceated and no values are passing into functions.
    Pro: code simplicity
    Con: conversion rates are hard coded inside functions. If a rate is needed again, need to hard code again, thus may result in discrepencies. Functions are not stand-alone.
    A US dollar value will be converted to Euro, Turkish Lira and Chinese Yuan through three function calls.
First Create Date: September 6, 2023
Last Update Date: January 30, 2024
Author: Lingma Lu
Version: 1.1
"""

#create variables to store the currency value in dollars
currencyDollarValue = 10;


#define a function to convert the dollar value to Euro
def convertEuro():
    return currencyDollarValue*0.93;

#define a function to convert the dollar value to Turkish Lira
def convertTurkishLira():
    return currencyDollarValue*26.78;

#define a function to convert the dollar value to Chinese Yuan
def convertChineseYuan():
    return currencyDollarValue*7.32;


#function calls
print(str(currencyDollarValue) + " dollars converted to Euro is " + str(convertEuro()));
print(str(currencyDollarValue) + " dollars converted to Turkish Lira is " + str(convertTurkishLira()));
print(str(currencyDollarValue) + " dollars converted to Chinese Yuan is " + str(convertChineseYuan()));
