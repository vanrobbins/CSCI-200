"""
File name: keyboardInput.py
Purpose: This file demonstrated code reusability and keyboard inputs
First Create Date: July 3, 2023
Last Update Date: September 10, 2023
Author: Lingma Lu
Version: 1.1
"""

#several functions were defined in the convertGrade.py file, thus import the file as a module to use functions defined
import convertGrade;

aScore = 89;
print("Your letter grade is: " + convertGrade.refinedConvert(aScore));

#Keywords inputs
name = input("What is your name?\n");

score = input("Hello! " + name + ". Please enter a percentage score and I will convert it into a letter grade based on the follow:\n90 - 100: A\n80 - 89: B \n70 - 79: C \n60 - 69: D \n<60: F\n\n");

score = float(score); #keyboard inputs are string types, thus need to convert to numeric values

if (score > 100 or score < 0): 
    print("Please enter a valid score. Execution aborted.");
else: print("Your letter grade is " + convertGrade.refinedConvert(float(score)));
