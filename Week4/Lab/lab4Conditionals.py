"""
File Name: lab4Conditionals
Purpose: 
    Design a program that will perform tasks based on at least two user selections or entries, e.g. user will select from a list of choices presented, and enter another input to generate outputs.
    Create a shape.
Special Requirements: 
    Ask for at least two keyboard inputs
    If/else structure is used. 
    Each choice is defined as a function and the functions are called in the executable file.
    Have a utility file and group all the function definitions in this file. 
    Take invalid inputs into considerations. E.g. if an input should be numeric, only process the input if it is indeed numeric. 
Variables Used In the Order of Creation:
 shape: local variable in chooseShape is defined to users input 
 validShape: local array in chooseShape stores valid inputs for shape, ensures that users input is a valid 
First Created: 9/21/2024
Last Updated: 9/23/2024
Author: Van Robbins
Version 1.0
"""
#Import utility file
import lab4Shapes;

#Function asks user for shape and ensures entry is valid
def chooseShape():
    validShape=["1","2","3"];
    print("What shape would you like to draw?");
    shape=input("1| Square\n2| Rectangle\n3| Equilateral Triangle\n");
    #Checks for valid entry
    #Valid entry: Converts to int and sends to makeShape
    if shape in validShape: 
        shape=int(shape);
        lab4Shapes.makeShape(shape);
    #Invalid Entry: Recalls function for user to try again
    else: 
        print("Please pick a valid shape by entering a number 1-3\n");
        chooseShape(); 

#RUNS MAIN FUNCTION
chooseShape();

