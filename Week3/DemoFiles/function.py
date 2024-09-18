"""
File Name: function.py
Purpose:
    This file demonstrates the use of functions. Topics include function defintion, function call, inputs and return valurs,
    parameters and arguments, variable scopes
First Create Date: July 3, 2023
Last Update Date: September 2, 2023
Author: Lingma Lu
Version: 1.1
"""

#---------------------------------------------------------------------------------------------------------------------------
#In the context of programming, a function is a named sequence of statements that performs
#a specific task. When you define a function, you specify the name, input parameters and the sequence of
#statements. Later, you can “call” the function by name, and give different input values as arguments.
#Functions are specified through a name following by a pair of parentheses.
#If a function produces a value, the value can be passed out of the function, i.e. this function "returns" a value.
#print() and type() are two built-in functions which have been defined in the Python language package, thus you can simply
#call them whenever you need to use them.
#--------------------------------------------------------------------------------------------------------------------------

#function calls with one input
a = 3;
print(a);
print(a+1);
print(type(42+5.0));

print("\n");

#Functions may return (generate) values.
b = int(a+0.5); #int() will change a floating-point type to integer type by chopping of the fraction part. The returned value is stored in b.
print(b);
c = float(36); #change an integer to a float type
d = float('3'); #change a string to a float type
#d = float('a'); #This will result in an error.
print("cccccccc ddddddd is " + str(c) + " and d is " + str(d));
e = print("c is " + str(c) + " and d is " + str(d));
print("eeeeeeeee " + str(e)); #print() does not return a value. It simply performs a task. Thus the value of e is "None"
t = type(5.0);
print("ttttttttt " + str(t)); #type() returns a value.

print("\n");

#Functions of similar nature or purpose can be grouped into a module (file).
#Must import the module before using that function.
import math; #A number of mathematical functions are defined and grouped into a module called "math".
print(math.sqrt(2)); #Use the dot notation to specify the module, which means calling the function sqrt() defined in that module.

print("\n");

#--------------------------------------------------------------------------------------------------------------
#User can define functions.
#Function definition:specify what the function is like and what it should do
#Function call: run the function
#Must first define the function before calling it.
#First line is called "header", starting with def, followed by function name and input parameters, ending with a ":".
#Rest of the lines are called "body", indended by convention with 4 spaces, ending with a blank line.
#-------------------------------------------------------------------------------------------------------------

#This function takes no input and returns no value; it simply prints out two lines.
def bark():
    print("woof!");
    print("woof woof!!");


bark(); #function call

#This function defines one "parameter". When it is called, it will take only one input.
def square(x):
    r = x*x;
    print("square of " + str(x) + " is " + str(r));
    #print("square of " + str(x) + " is " + str(x*x));

square(3); #When the function is called, the actual value passed into the function is called an "argument".
square(4);

#This function defines two parameters.
def power(x, y):
    print(x**y);

power(2,3); #Two arguments are passed to the function.
a = 2;
b = 4;
power(a,b);


#---------------------------------------------------------------
#Functions returning values are called "fruitful functions".
#Return type is determined by the value.
#--------------------------------------------------------------

#This function returns the area of a circle with the given radius.
def areaOfCircle(radius):
    a = math.pi * radius ** 2;
    return a;

print(f"The area is of the circle with radius 2 is {areaOfCircle(2)}");
#The returned value is used as an input to the print() function

#Returned value can be assigned to another variable.
a = 3;
b = areaOfCircle(a);
print(b);

#It is better to rewrite the square() and power() function and have them return values, since they both generate values.
#Having functions return values provides flexibility in using functions.
def newSquare(x):
    r = x*x;
    return r;

print("=======The square of 3 is " + str(newSquare(3))); #can print out the result
y = newSquare(4); #can store the result into a variable and use it later

def newPower(x, y):
    return x**y;

a = 2;
b = 3;
print(newPower(a,b)); #variables can be used as function arguments

print("\n");


#A function can be called inside another function.
def doMath(x):
    print("The value to be used is " + str(x)); #Is x changed to a string type?
    y = areaOfCircle(x); #areaOfCircle() function is defined above
    print("The area is " + str(y));

print("Begin the program");
doMath(2);
doMath(3);

print("Done\n"); #prints a new line after printing "Done"

print("\n1111111111111111111\n");

#------------------------------------------------------------------------------------------------------------------#
"""
Variable Scopes:
- The scope of a variable is where the variable can be used (accessible).
- The scope of a variable is determined by the location where it is created.
- Local Scope: If a variable is defined (created) inside a function, it is called a local variable. It has local scope. It is accessible (can be used) only inside the function.
- Global Scope: If a variable is defined (created) outside a function, it is a global variable. It has global scope. It is accessible (can be used) anywhere in the file (inside of functions as well).
"""
#------------------------------------------------------------------------------------------------------------------#

#global variable x and y, defined outside of a function
x = 2;
y = 3;

#local variable a and b, defined inside the function square1()
def square1(a):
    b = a*a;
    return b;

y = square1(x);
print("The square of " + str(x) + " is " + str(y));

print("\n222222222222222222222\n");

#variables belong to different scopes can have the same name. They are different variables.
x = 4;
y = 5;

def square2(x): #local variable x is created
    y = x*x; #local variable y is created; local variable x is used(accessed)
    return y; #local variable y is accessed


y = square2(x); #global variable x is used to pass value into square2(); value of local y is passed out of square2() and given to global variable y
print("The square of " + str(x) + " is " + str(y));

print("\n3333333333333333333333\n");

x = 6;
y = 7;

def square3(x): #local x is created
    x = x*x; #using the lobal x then update the local variable
    print("x inside the square3 function is " + str(x));
    return x; #value of local x is passed out of the function

x = square3(x); #value of global variable x is passed into the function and the return value is used to update the global x
#global x value is updated outside of the function
print("x outside the square3 function is " + str(x));

print("\n44444444444444444444444\n");

#A global variable can be used anywhere
x = 8;
y = 9;

def square4():
    y = x*x; #no local variable can be found. program will check if there is a global variable called x, if so, use the global variable
    return y; #local y is created in line above and used here

print("square4 returned value is: " + str(square4())); #returned value is being printed out instead of being assigned to a variable

print("\n55555555555555555555555555\n");


x = 10;
y = 11;

def square5():
    global x; #announce that x in this scope is the global x
    print("xxxxxxxx global x value is:: "+ str(x));   #no local variable can be found. program will check if there is a global variable called x, if so, use the global variable
    y = x*x; #local y is created, global x value is used; y was never announced as a global variable, thus when a variable y is required to hold a value, local y is created.
    x = 13; #global x value is updated inside the function
    print("xxxxxxxx global x is changed to: "+ str(x));
    return y;

print("square5 returned value is: " + str(square5()));
print("-------------global x value is: " + str(x)); #the value was updated in line 210

#This line will result in an error, as the program will try to create a local variable x, instead of changing the value of the global variable.


print("\n666666666666666666666666\n");

x = 12;
y = 13;

def square6():
    print("xxxxxxxx global x is used: "+ str(x));   #no local variable can be found. program will check if there is a global variable called x, if so, use the global variable
    y = x*x; #local y is created, global x value is used; y was never announced as a global variable, thus when a variable y is required to hold a value, local y is created.
    #x = 11; #turn on this line will result in an error
    #A variable is required to hold a value, program will create a variable called x, since it is created here, it will be a local x. Same idea as creating a local y.
    #However, x was recognized as a global variable through line 226, thus will result in an error.
    #A variable cannot exists both as a local and global in a particular scope.
    return y;

print("square6 returned value is: " + str(square6()));


"""
Notes on using global variables:
1. Avoid using global variables, as 1)it may be accidentally changed inside other functions, 2)local variables will be destroyed as soon as a function call is complete thus result in better code efficiency.
2. If values need to be used inside a function, consider passing values into the function.
3. Only use global variables when it is absolutely necessary, considerations include size of the code package, variable size, how many times a variable needs to be accessed, available memory space etc.
"""

"""
Why functions?
1. Package statements that performs one task - code organization.
2. A function can be defined once and used at any time by anybody - code reusability. Don't reinvent the wheel!
3. If codes need to be updated, only need to update once inside the function definition.
4. Better team work - one member creates the function for others to use; others only need to know the function header and return type.
"""
