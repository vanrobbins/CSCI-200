"""
File Name: lab3Functions
Purpose: 
    Design and create a python program that given three numbers outputs the numbers in order and says when they were inputed.
Special Requirements: 
    Have at least 3 user defined functions
    At least one function is called within another function
    At least one function takes two parameters
    At least one function returns a value
    At least one global variable is used and accessed inside a function
Variables Used In the Order of Creation:
    num1: global variable will be the first number inputed
    num2: global variable will be the second number inputed
    num3: global variable will be the third and final number inputed
    correctOrder: global array that is initially initialized empty, will later store results
    first: local variable of compare is the first number entered into the function
    second: local variable of compare is the second number entered into the function
    small: local variable of compareAll is initially the smaller of the two numbers from compare, later set to actual smallest number
    big: local variable of compareAll is initially the bigger of the two numbers from compare, later set to actual biggest number
    unknown: local variable of compareAll has yet to be compared to the other two numbers
    mid local: variable of compareAll is initialized will later be set to the middle number
    findEntry: local variable of order is compared to the initial numbers entered to find when it was entered

First Created: 9/12/2024
Last Updated: 9/17/2024
Author: Van Robbins
Version 1.0
"""
#Entered Numbers
num1= int(input("Enter an integer "));
num2= int(input("Enter another integer "));
num3= int(input("Enter a third integer "));
#Initialized array for results 
correctOrder=[];


#Main function that finds if the first or second number entered is larger, calls compareAll function with the two numbers in small to large order
def compare(first,second):
    if  first<second:
        return compareAll(first,second,num3); #Uses global variable num3
    else:
        return compareAll(second,first,num3); #Uses global variable num3

#Compares the numbers and puts them into correct order in array
def compareAll(small,big,unknown):
    if big<unknown: #small<big<unkown
        mid=big;
        big=unknown;
    elif small<unknown: #small<unknown<big
        mid=unknown;
    else: #unkown<small<big
        mid=small;
        small=unknown;
    return small, mid, big;

#Finds which number was entered when, returns a string given when the number was entered or the order
def order(findEntry):
    if findEntry==num1: #Uses global variable num1
        return "1st number entered";
    elif findEntry==num2: #Uses global variable num2
        return "2nd number entered";
    else:
        return "3rd number entered";
    
#Makes sure no numbers are equal to one another
if num1==num2 or num1==num3 or num2==num3: 
    print("Try again! Enter three different integers");

#Only runs if 3 unique integers
else: 
    #correctOrder calls the compare function and then hence forth the compareAll function
    correctOrder=compare(num1,num2); #small is at the index of 0 in the correctOrder array, mid is at the index of 1, and big is at the index of 2
    print(f"The Smallest number is {correctOrder[0]} it was the {order(correctOrder[0])}")#order returns when the smallest number was entered
    print(f"The Middle number is {correctOrder[1]} it was the {order(correctOrder[1])}")#order returns when the middle number was entered
    print(f"The Largest number is {correctOrder[2]} it was the {order(correctOrder[2])}")#order returns when the largest number was entered