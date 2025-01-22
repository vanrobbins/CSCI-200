"""
File name: recursion.py
Purpose: This file demonstrates recursion
Author: Lingma Lu
Create date: 11/05/2023
Last update date:11/18/2024
version: 1.1
"""

#count how many characters in a string - write your own string length function
#similar to the problem "count how many people in a line"

callCount = 0; #this variable is used to see how many times the function is called
#print(len(title));

def lengthOfString(s):
    if (s == ""):
        return 0;
    else:
        return lengthOfString(s[1:]) + 1;

print(lengthOfString("CSCI"));


print("*****************");

#the following is an extended version of the above, with printouts to trace the function calls
def lengthOfStringWithTrace(s):
    global callCount;
    callCount = callCount + 1;
    print("\nNew function call. callCount value:  " + str(callCount));
    print("Process string - " + s + ". Waiting for a result ...");

    if (s == ""):
        print("Empty string. Length is 0.\n ");
        return 0;
    else:
        print("In else. going to process " + s[1:]);
        reportBack = lengthOfStringWithTrace(s[1:]) + 1;
        print("In else, finished processing " + s[1:] + " length is " + str(reportBack));
        return reportBack;

print("\nLength of string CSCI is " + str(lengthOfStringWithTrace("CSCI")));

print("====================\n");
#n factorial example
#4!: 4*3! = 244
#...
#1!: 1
def factorial(n):
    if (n == 1):
        print(str(n) + " factorial is 1");
        return 1;
    else:
        print("Going to find " + str(n-1) + " factorial");
        res = n*factorial(n-1);
        print(str(n) + " factorial is " + str(res));
        return res ;

print("xxxxxxxxxxxxxxxxxxx n factorial example: ");
n = 4;
if (n >= 1):
    print("Function call - " + str(n) + " factorial is " + str(factorial(n)));

#Fibonacci sequence example
#Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
def fibonacci(n):
    if (n == 0):
        return 0;
    else:
        if (n == 1):
            return 1;
        else:
            return fibonacci(n - 1) + fibonacci(n - 2);
print("Fibonacci sequence example: ");
x = 8;
if (x >= 0):
    print("The number in position " + str(x) + " is " + str(fibonacci(8)));

#recursive vs iterative

#find string length using a for loop
def findLength(s):
    count = 0;
    for k in s:
        count = count + 1;

    return count;

print("\ncount length using for loop");

title = "CSCI";
print(findLength(title));

#n factorials
def factorialInteration(n):
    result = 1;
    count = 1;
    while (count <= n):
        result = result * count;
        count = count + 1;

    return result;

print("\nfactorial using while loop:");
print(factorialInteration(4));