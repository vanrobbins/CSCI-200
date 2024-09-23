"""
File Name: conditionals.py
Purpose:
    This file introduces the following concepts:
    a. floor division operator and modulus operator
    b. boolean expressions and relational operators
    c. logical operators
    d. if/else structures
    e. nested conditionals and chained conditionals
    f. pseudocodes
First Create Date: July 3, 2023
Last Update Date: July 14, 2024
Author: Lingma Lu
Version: 1.1
"""

#floor division operator // divides two numbers and rounds down to an integer
minutes = 105;
hours = minutes / 60;
print("hours is " + str(hours));
hours = minutes // 60;
print("hours is " + str(hours));

print("\n");

#modulus operator %  divides two numbers and returns the remainder
remainder = minutes % 60;
print("remainder is " + str(remainder));

#extract the right-most digit(s) from a base 10 number
print("The right-most digit is:" + str(238%10));
print("The right-most digits are:" + str(238%100));

print("\n");

#boolean expression is an expression that evaluates to either True or False
x = True; #case sensitive
y = False;
#x = true; #This is a syntax error
print(type(x));
print("x is " + str(x));
print(type(y));
print("y is " + str(y));
z = "True"; #What is the type of z?

print("\n");

# == is a relational operator, means "equal to"
a = 3; b = 3;
c = a == b; # more readable version: c = (a == b);
print("Type of c is: " + str(type(c)));
print("Is a equal to b? " + str(c));

#other relational operators
c = 4; #c is changed to an integer type variable
print("Is a equal to c? " + str(a == c));
print("Is a not equal to c? " + str(a != c)); #not equal: !=
print("Is a greater than c? " + str(a > c));
print("Is a smaller than b? " + str(a < b));
print("Is a greater than or equal to b? " + str(a >= b));
print("Is a smaller than or equal to c? " + str(a <= c));

print("\n");

#logical operators: and, or
#used when evaluating compound expressions

#"and" operator: both expressions have to be evaluated to True for the compound expression to be evauated to True; all other cases will be evaluated to False.
#example 1: a person will be approved for a credit card application if having a credit score of over 550 and an annual income above $25000
scoreRequired = 550;
incomeRequired = 25000;
creditScore = 525;
income = 35000;
approve = creditScore >= scoreRequired and (income >= incomeRequired); #first expression evaluated to be False, second expression evaluated to True
#more readable version:
#approve = (creditScore >= scoreRequired) and (income >= incomeRequired);
print("11111111First approve: " + str(approve));


#"or" operator: at least one expression must be evaluated to True for the compound expression to be evaluated to True.
#Both have to be False for the compound expression to be evaluated to False. All other cases will be evaluated to True.
#example 2: a person will be approved for a credit card application if either having a credit score of over 600 or an annual income above 50000
scoreRequired = 600;
incomeRequired = 50000;
creditScore = 625;
income = 35000;
approve = (creditScore >= scoreRequired) or (income >= incomeRequired); #first expression evaluated to be True, second expression evaluated to False
print("2222222Second approve: " + str(approve));

#if both "and" and "or" are used in the compound expression, "and" takes precedence
#example 3: a person will be approved for a credit card application if either having a credit score of over 600 or an annual income above 50000, and a debt to credit ratio lower than 60%
#similar to 2 + 6 / 3
# (2 + 6) / 3

scoreRequired = 600;
incomeRequired = 50000;
creditRadioRequired = 0.6;
creditScore = 625;
income = 65000;
creditRatio = 0.65;
approve = (creditScore >= scoreRequired) or (income >= incomeRequired) and (creditRatio <= creditRadioRequired);
#                                             (         T                 and                F                 )
#                    T                   or                                     F
#                                         T

#The above is equivellent to:
approve = (creditScore >= scoreRequired) or ((income >= incomeRequired) and (creditRatio <= creditRadioRequired)); #True or (True and False)
print("33333333Third approve: " + str(approve)); #should be False because of the higher credit ratio, however, the result is True, because "and" take precedence
#should be written as:
approve = ((creditScore >= scoreRequired) or (income >= incomeRequired)) and (creditRatio <= creditRadioRequired);
#         (            T                  or               T           )
#                                         T                              and              F
#                                                                        F
print("44444444Fourth approve: " + str(approve));

#"and", "or" operators perform short-circuit evaluations - if the result can be determined without evaluating further, the evaluation process will stop
#Short-circuit evaluations improves code performance and prevent run time errors
#The above is better to be written as below, because if the first condition is false, there is no need to further evaluate
approve = (creditRatio <= creditRadioRequired) and ((creditScore >= scoreRequired) or (income >= incomeRequired));
#                     F                        and    ????
#                                              F
print("55555555Fifth approve: " + str(approve));

print("\n\n");

#"not" operator, negates the boolean value
a = 3; b = 4;
c = not True;
print(type(c)); #prints the type of c
print("c is " + str(c)); #prints the value of c
d = not(a == b);
print(type(d));
print("d is " + str(d));
print("\n");


#conditional execution: use if/else structure to determine the flow of execution of a block of codes
#"if" is followed by a condition or compound condition, if the condition is evaluated to True, the if block runs
#otherwise, the "else" block runs
#an "if" structure doesn't have to be followed by an "else" structure
a = 1;
b = 2;

if (a == b):
    print("a is equal to b"); #this line is not printed, because the condition is evaluated to False

if (a != b):
    print("a is not equal to b"); #this line is printed, because the condition is evaluated to True

if (a == b):
    print("a is equal to b");
else: #else must be on its own line followed by ":"
    print("a is not equal to b");


print("\n");

#Example: determine the letter grade based on the percentage score:
#A: 90 - 100, B: 80 - 89, C: 70 - 79, D: 60- 69, F: <=59
def convert(score):
    if (score >=90 and score <=100):
        print("A");
        print("Great job!");
    if (score >=80 and score <=89):
        print("B");
        print("Good job!");
    if (score >=70 and score <=79):
        print("C");
        print("Not bad!");
    if (score >=60 and score <=69):
        print("D");
        print("You passed!");
    if (score <=59 and score >= 0):
        print("F");
        print("I am sure you will do better next time!");
    if (score >100 or score <= 0): #always plan for unusual inputs
        print("Please enter a valid score.");

print("\ncall convert():");
aScore = 95;
convert(aScore);
aScore = 61;
convert(aScore);
aScore = 101;
convert(aScore);

#Although the convert() function generates correct result, all the "if" conditions are evaluated, thus has poor code performance.
#Below is a better version, using nested conditions (if/else structure nested inside another if/else structure)
#Pay attention to the indentations.
def betterConvert(score):
    if (score >100 or score <= 0):
        print("Please enter a valid score.");
    else:
        if (score >=90 and score <=100): #continue only if the score is valid
            print("A");
            print("Great job!");
        else: #else must be on its own line followed by ":"
            if (score >=80 and score <=89):
                print("B");
                print("Good job!");
            else:
                if (score >=70 and score <=79):
                    print("C");
                    print("Not bad!");
                else:
                    if (score >=60 and score <=69):
                        print("D");
                        print("You passed!");
                    else:
                        if (score <=59 and score >= 0):
                            print("F");
                            print("I am sure you will do better next time!");
print("\ncall betterConvert():");
aScore = 95;
betterConvert(aScore);
aScore = 61;
betterConvert(aScore);
aScore = 101;
betterConvert(aScore);

#the above can be simplified using the "elif" keyword. It is called a "chained conditional expression".
#The codes are not further indented, since it is not a nested structure.
def chainConvert(score):
    if (score >100 or score <= 0):
        print("Please enter a valid score.");
    elif (score >=90 and score <=100): #continue only if the score is valid
        print("A");
        print("Great job!");
    elif (score >=80 and score <=89):
        print("B");
        print("Good job!");
    elif (score >=70 and score <=79):
        print("C");
        print("Not bad!");
    elif (score >=60 and score <=69):
        print("D");
        print("You passed!");
    elif (score <=59 and score >= 0):
        print("F");
        print("I am sure you will do better next time!");

print("\ncall chainConvert():");
aScore = 95;
chainConvert(aScore);
aScore = 61;
chainConvert(aScore);
aScore = 101;
chainConvert(aScore);
chainConvert(aScore);
aScore = 61;
chainConvert(aScore);
aScore = 101;
chainConvert(aScore);
