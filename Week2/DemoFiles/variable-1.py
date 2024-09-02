"""""""""""""""""""""""""""""""""""""""""""""""""""
This file demonstrates key concepts about variables
"""""""""""""""""""""""""""""""""""""""""""""""""""

#variable types,what type of variables are they?
#In Python, you don't need to specify what type of variables you are creating, but it will be good note them via comments.
#The type is determined by the value assigned to the variable.
message =  "And now for something completely different"; #string type
m = ""; #two quotes together means an empty string, a string of length 0
m = " "; #a string of lenght 1, the value is "a blank space"
n = 17;  #integer type
pi = 3.1415926535897932; #float type
print(n);
n = "new"; #When you change the type of the value, a new variable is created, even if the name is the same  (a new memory space is allocated with the new value, with the same label).
print(n);

print("\n");

#"=" is an assignment operator, it reads "gets"
#The right side of the "=" is evaluated first, the result will be assigned to the variable on the left side.
a = 5; #read as "a gets 5"
b = 3;
c = a + b; #c gets the sum of a and b, what is the type of c?
print("c is:" + str(c)); #Must convert c to a string before using the + operator, because the first part is a string. This is called "string concatenation".

print("\n");

#What is the result of d below?
a = "5";
b = "3";
d = a + b; # + sign used for strings concatenation
print("d is:" + d); #string concatenation again


#What is the result of e below?
"""
a = "5";
b = 3;
e = a + b;
print("e is:" + e);
"""

print("\n");


#varialbe names
#Choose names that are readable and meaningful.
#Variable names are case-sensitive.
#variable names can contain only letters and numbers but cannot begin with a number.
#Follow a naming convention, below is called camel-case notation (https://en.wikipedia.org/wiki/Camel_case).
centimeterValue = 20; #common naming convention: use camel notation
CentimeterValue = 30; #another variable is created, avoid doing this, and be careful about typoes
print(centimeterValue);
print(CentimeterValue);

print("\n");

meter_value = centimeterValue/100;
#Another naming convention: use only lower cases and use _ to seperate words
#Choose a convention and stick to it.
#It is important to have a consitant coding style.
print("meter value is " + str(meter_value) + ".");
#use escape characters when printing quotes.
#"\" is an escape character, which means the character after "\" is a character as is.
print("meter value is \"" + str(meter_value) + "\"."); #The second and the firth double quotes should not be interpreted as "closing out the string"
print('meter value is \'' + str(meter_value) + '\'.');
print('meter value is "' + str(meter_value) + '".'); #mix single quotes and double quotes to avoid using escape characters


#cannot create variables whose names are the same as keywords
#Keywords are part of the Python infrustructure.
#Below is illegal:
#print = 2;
#print(print);

print("\n");

#An expression is a statement that contains variables, values and operators and can be evaluated to a result.
#what does the following block do?
miles = 26.2;
message = "A marathon is " + str(miles * 1.61) + " kilometers.";
print(message);

print("\n");

#hard coding: a value is typed out in the code, rather than being obtained through computation or user input
distanceMile = 2;
print(str(distanceMile) + " miles in kilometer is " + str(distanceMile * 1.6)); #none hard coding to print out the distance in kilometer
print("2 miles is equal to 3.2 kilometers");

#another example in hard coding
username = "abc";
passcode = "123";
#none hard coding - obtain values from the user inputs
#Hard coding can be used for testing purposes, e.g. for testing out logic.

print("\n");

# ** used with numbers means exponentiation
# * used with strings means repetition
print(2**3);
print("x"*4);





