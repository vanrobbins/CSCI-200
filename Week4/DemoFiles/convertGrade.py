"""
File Name: convertGrade.py
Purpose:
    This file serves as a utility file doing letter grade conversions. It defined several functions to be used by files doing grades conversions.
First Create Date: July 3, 2023
Last Update Date: July 8, 2023
Author: Lingma Lu
Version: 1.1
"""

#conditional execution: use if/else structure to determine the flow of execution of a block of codes
# "if" is followed by a condition or compound condition, if the condition is evaluated to True, the if block runs
# otherwise, the "else" block runs
# an "if" structure doesn't have to be followed by an "else" structure
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

#The above can be simplified using the "elif" keyword. It is called a "chained conditional expression".
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


#A more reusable version
def refinedConvert(score):
    if (score >100 or score <= 0):
        return "Invalid score.";
    elif (score >=90 and score <=100): #continue only if the score is valid
        return "A";
    elif (score >=80 and score <=89):
        return "B";
    elif (score >=70 and score <=79):
        return "C";
    elif (score >=60 and score <=69):
        return "D";
    elif (score <=59 and score >= 0):
        return "F";