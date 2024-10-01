"""
File Name: lab5Utility
Purpose: 
Act as utility to main file

First Created: 9/28/2024
Last Updated: 10/1/2024
Author: Van Robbins
Version 1.1
"""

def check(sizeInput,validInputBottom,validInputTop):
    current=validInputBottom;
    validSize=[];
    while current<=validInputTop:
        validSize.append(str(current));
        current+=1;
    if sizeInput not in validSize: #Checks input with array of valid inputs
        print(f"The input must be between {validInputBottom} and {validInputTop}");
        again=input("Would you like to try again Y/N\n");
        if(again.upper()=="Y"):
            return "goAgain";
        else:
            return False;
    else:
        return True;

def checkPositiveNonZero(enteredValue):
    #Checks that value can be converted into a number
    try:
        float(enteredValue);
    except ValueError:
        print("The input must be a number");
        again=input("Would you like to try again Y/N\n");
        if(again.upper()=="Y"):
            return "goAgain";
        else:
            return False;
    
    num=float(enteredValue);
    if num<=0: 
        print("The input must be greater than 0");
        again=input("Would you like to try again Y/N\n");
        if(again.upper()=="Y"):
            return "goAgain";
        else:
            return False;
    else:
        return True;

def checkInputLength(enteredString, maxLength):
    if len(enteredString)>maxLength:
        print(f"The input can not be longer than {maxLength} characters");
        again=input("Would you like to try again Y/N\n");
        if(again.upper()=="Y"):
            return "goAgain";
        else:
            return False;
    else:
        return True;

def amountEntry(data, divider):
    index = 0;
    count = 0;
    while (index < len(data)): #Search through data alloted and count the amount of 'divider' characters it contains
        if (data[index]) == divider:
            count+=1;
        index +=1;
    return count;

#Cuts string data based on the start and end's index, divides whole into parts based on divider
def cut(data,start,end,divider):
    dataCutToStart=data[start:];#Cuts Data from start index
    parsedData=[];#Empty array that will store parsed data
    index=0;
    start=0;
    if type(end)==int:#end is already defined as an index value
        end=end;
    else:#End is not a defined index but a character
        endEntryCharacter=end;
        end=dataCutToStart.find(endEntryCharacter);#Find first occurence of character from already the start of the data
    dataCut=dataCutToStart[start:end+1]; #Cuts data from start to found end+1 to include end character
    #Loop looks through cut data dividing data into parts based on given divider
    while index!=len(dataCut):
        if(dataCut[index])==divider:#If the character at the index of the data is the same as the divider append that part to array
            parsedData.append(dataCut[start:index]);
            start=index+1; #For next data part the start will be at the end of the last part
            index+=1;
        elif((dataCut[index])==endEntryCharacter) or (index==end):#Saves last part of data
            parsedData.append(dataCut[start:end]);
            index+=1;
        else: #Character is neither divider or end
            index+=1;
    return parsedData; #Returns each part of data in array entry