"""
File Name: scopeExample1.py
Purpose:
    This file demonstrates the use of functions and local variables.
    Key concept - passing values into functions.
    Pro: code simplicity
    Con: conversion rates are hard coded in functions. If a rate is needed again, need to hard code again, thus may result in discrepencies.
    A US dollar value will be converted to Euro, Turkish Lira and Chinese Yuan through three function calls.
First Create Date: September 6, 2023
Last Update Date: January 30, 2024
Author: Lingma Lu
Version: 1.1
"""

#create variables to store the currency value in dollars
currencyDollarValue = 10;


#define a function to convert the dollar value to Euro
def convertEuro(v):
    return v*0.93;

#define a function to convert the dollar value to Turkish Lira
def convertTurkishLira(v):
    return v*26.78;

#define a function to convert the dollar value to Chinese Yuan
def convertChineseYuan(v):
    return v*7.32;


#function calls
print(str(currencyDollarValue) + " dollars converted to Euro is " + str(convertEuro(currencyDollarValue)));
print(str(currencyDollarValue) + " dollars converted to Turkish Lira is " + str(convertTurkishLira(currencyDollarValue)));
print(str(currencyDollarValue) + " dollars converted to Turkish Chinese Yuan is " + str(convertChineseYuan(currencyDollarValue)));
