"""
File Name: lab4Shapes
Purpose: 
    Utility file for lab4Conditionals, defines various functions
Variables Used In the Order of Creation:
    selectedShape: is the shape picked by user
    sizeEq: is the size for a shape that has equal length and width
    sizeDiff: array that holds length and width of shape
    wlInput: inputed value from user for shape that has equal length and width
    wInput: inputed width value from user for shape that has different length and width
    lInput: inputed length value from user for shape that has different length and width 
    size: holds value in shapes functions for that is the size and width
    width: is used in loops to ensure that the correct amount of symbols are printed, used in various functions
    length: is used in loops to ensure that the correct amount of layers are printed and the correct layer is printed, used in various functions
    spaceInside: holds the amount of space needed to be printed inside triangle
    spaceOutside: holds the amount of space needed to be printed outside triangle
    count: used to count in loops, ensures correct amount of symbols are printed
    sizeW: used by rectangle holds wInput in function needed because different width and length
    sizeL: used by rectangle holds lInput in function needed because different width and length
First Created: 9/21/2024
Last Updated: 9/23/2024
Author: Van Robbins
Version 1.0
"""
#Finds size user wants shape, sends to respective function to make the shape
def makeShape(selectedShape):
    #Square and Triangle| 1 or 3
    if selectedShape==1 or selectedShape==3:
        sizeEq = sizeEqualWL(); #Runs function in utility asking user to enter size of sides
        while sizeCheck(sizeEq)!=True: #Ensures that size is valid will loop until entry is valid
            sizeEq = sizeEqualWL();
        else: #Size is valid
            sizeEq= int(sizeEq); #Converts size to int
            #SQUARE
            if selectedShape==1:
                square(sizeEq);
            #TRIANGLE
            else:
                triangle(sizeEq);
    #Rectangle |2
    else:
        sizeDiff = sizeDiffWL(); #Runs function in utility asking user to enter size of width and length3
        while sizeCheck(sizeDiff[0])!=True or sizeCheck(sizeDiff[1])!=True: #Ensures that both sides are valid will loop until entry is valid
            sizeDiff = sizeDiffWL();
        else: #Size is valid
            width= int(sizeDiff[0]); #Converts sides to int
            length= int(sizeDiff[1]);
            rectangle(width,length); #Calls rectangle function in 

#Size for one variable shape
def sizeEqualWL():
    wlInput=input("Please enter the length of one side of the shape or radius of the shape (3-10) ");
    return wlInput;

#Size for two variable shape 
def sizeDiffWL():
    print("Please enter the width and length of the shape of the shape (3-10) ");
    wInput=input("Width: ");
    lInput=input("Length: ");
    return wInput,lInput; #Returns inputs and

#Checks to see if a size is valid
def sizeCheck(sizeInput):
    validSize=["3","4","5","6","7","8","9","10"]; #Array of valid inputs
    if sizeInput not in validSize: #Checks input with array of valid inputs
        print("Try again! The size must be between 3 and 10");
        return False;
    else:
        return True;

#SQUARE
def square(size):
    width=size; #New variable used to count for loops ensures shape is correct width
    height=size; #New variable used to count for loops ensures shape is correct height
    while(height>0): #If height is not 0 will repeatedly run

        #Between top and bottom of shape
        if height<size and height>1: 
            width=size-1; #Ensures that width is reset so correct amount of symbols are printed minus the left outer symbol
            print("⬜",end=''); #Prints left outer symbol
            while(width!=1): #Prints spaces until reach other outer symbol
                print("  ",end='')
                width-=1;
            print("⬜"); #Prints right outer symbol and starts new line
            height-=1; #Subtracts 1 from height this layer of the shape is complete
        
        #If height is the top or bottom will run
        else: 
            width=size; #Ensures that width is reset so correct amount of symbols are printed
            while(width>0):
                print("⬜",end=''); #Prints # on same line while loop is valid
                width -=1; #Subtracts 1 from width every time symbol printed
            height-=1; #Subtracts 1 from height this layer of the shape is complete
            print("");  #Creates new line to ensure top of shape is on its own line

#TRIANGLE
def triangle(size):
    spaceInside=0;
    spaceOutside=size-1;
    width=size-2; #Only used to solve base, subtract two to subtract sides
    height=size;
    count=0;
    while(height>0): #loops until height is no longer greater than 0
        count=0; #ensures count for counting spaces in loops is correctly set to 0

        #Prints all sides except for bottom
        if height>1: 
            # Loop prints proper outer spaces to left side of triangle
            while(spaceOutside>count): 
                print(" ",end='');
                count+=1;
            print("/",end=''); #Prints out left side after spaces
            count=0; #Resets count to be used to find proper inner space
            #Loop prints inside spaces of triangle
            while(spaceInside>count): 
                print(" ",end='');
                count+=1;
            print("\\");#Prints out \, right side
            spaceOutside-=1; #Removes 1 outerspace so sides move in for next layer
            spaceInside+=2; #Adds 2 spaces in between sides for next layer
            height-=1; #layer of the shape is complete moves to next layer
        
        #Only runs if last layer of shape
        else: 
            print("/",end=''); #left outer edge
            while(width>=0):
                print("＿",end=''); #Prints long _ to meet right bottom edge
                width -=1; 
            print("\\",end=''); #Prints out single \, right outer side
            height-=1; #Height should now equal 0 signifying the end of loop

#RECTANGLE
#Very similar to square just width and height are set to 2 different values
def rectangle(sizeW, sizeL):
    width=sizeW;  #New variable used to count for loops ensures shape is correct width
    height=sizeL; #New variable used to count for loops ensures shape is correct height
    while(height!=0):

        #Between top and bottom of shape
        if height<sizeL and height>1: 
            width=sizeW-1; #Ensures that width is reset so correct amount of symbols are printed minus the left outer symbol
            print("⬜",end=''); #Prints left outer symbol
            while(width!=1): #Prints spaces until reach right outer symbol
                print("  ",end='')
                width-=1;
            print("⬜"); #Prints right outer symbol and starts new line
            height-=1; #layer of the shape is complete moves to next layer
        
        #Prints if top or bottom of shape
        else: 
            width=sizeW;
            while(width>0):
                print("⬜",end='');
                width -=1;
            height-=1;
            print(""); #Creates new line to ensure top of shape is on its own line