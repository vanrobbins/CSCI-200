"""
File Name: lab7Utility
Purpose:
Serve as utility file for lab 7 

Median function finds median given a string that contains numbers

First Created: 11/1/2024
Last Updated: 11/5/2024
Author: Van Robbins
Version 1.0
"""
def median(stringWNums,divisor):
    floats=[]
    medianSum=0;
    #Seperates each word of string given proper divisor for string
    for i in stringWNums.split(divisor):
        #Trys to turn word/number into float
        try:
            floats.append(float(i));
        except:
            pass;
    #Finds sum of floats
    medianSum=sum(floats);
    #Finds median of floats and rounds to 2 decimal places
    median=round(medianSum/len(floats),2);
    return median;