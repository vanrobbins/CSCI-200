"""
File name: file.py
Purpose: This file demonstrates file processing
Author: Lingma Lu
Create date: 07/15/2023
Last update date:8/15/2024
version: 1.1
"""

#--------------------------------------------------------------------
#File Write
#-------------------------------------------------------------------
#Open a file in write mode, if no such file exists, will create a new one,
#otherwise, will wipe out old contents and put new contents in.
#If no directory is specified, will create a file in the same directory as this file.
#function open() will return a file object that provides methods for working with the file
#File Handling modes - r, w, a, x
#https://www.w3schools.com/python/python_file_handling.asp

fout = open("output.txt", 'w'); #write mode, create a file to write to, if the file doesn't exist, create one, otherwise, overwrite all contents
line1 = "This here's the wattle,adfdsafdsfdsafasdfdsafdsfd \n";

fout.write(line1); #write() will write the input to file
fout.write("the emblem of our land.\n"); #call write() again will keep writing to the file

#when you are done writing, close the file to clear out all memory spaces occupied by the file object
fout.close();
#fout.write("again"); #this will generate an error since the file object no longer exists.

#example, create a .csv file along with data

from datetime import date; #import the date module so as to use methods associated with date/time processing, e.g. date.today() on line 61

i = 0;
cityNames = ["Indianapolis", "New York", "Tokyo", "London"];
distanceChart = [[0, 648, 6476, 4000],[648, 0, 6760, 3470],[6476, 6760, 0, 5956],[4000, 3470, 5956, 0]];

fw = open("distance.csv",'w'); #csv means "comma seperated values". This type of text file is used to define data in tabular format, and can be opened by Spreadsheet software.
#first, write the column header, data is in cityNames list
for i in range(len(cityNames)):
    if (i == len(cityNames)-1):
        fw.write(cityNames[i]+'\n');
    else: fw.write(cityNames[i]+','); #if it is the last value in the row, add a carriage return, otherwise, add a comma after the value

#Set i back to 0 so it can be reused in a new loop
i = 0;

#loop through the 2D array and write values in the distanceChart into the csv file
while (i < len(distanceChart)):
    oneRow = distanceChart[i]; #get each row from the outer loop
    j = 0;
    while (j < len(oneRow)):
        oneValue = distanceChart[i][j]; #get each value from a row
        #print(oneValue); #it is always a good idea to print to console to check values
        if (j == (len(oneRow)-1)):
            fw.write(str(oneValue)+'\n'); #write() takes a string as input
        else: fw.write(str(oneValue)+','); #if it is the last value in the row, add a carriage return, otherwise, add a comma after the value
        j = j + 1;

    i = i + 1;


fw.write("Author: Lingma Lu; Date: " + str(date.today()));
#more about working with date and time - https://docs.python.org/3/library/datetime.html

fw.close();

#--------------------------------------------------------------------
#File read
#-------------------------------------------------------------------

#read the data in the file just created and construct a 2D array from it
fr = open("distance.csv",'r'); #open the file in read mode, if file doesn't exit, run time error will occur
print("xxxxxxxxxxxxxxxxxx\n");

print(fr.readline()); #read one line
print(fr.readline()); #read one line again

print(fr.read()); #read() will read all the characters and lines in the file including '\n', starting from where the file pointer points to, in this case, read the rest of lines

print("yyyyyyyyyyyyyyyyyyy\n");

fr.close();

#reconstruct the 2D array
newDistance = [];

frd = open("distance.csv",'r');

#read the first line and construct the cityNames array
#each time a line is read, the interator pointer will point to the next line
newCityNames = frd.readline().split(','); #use split() to transform a string into an array
print(newCityNames); #when printing to the console, \n will be interpreted as a chariage return, but when reading the value as text, \n is part of the string


lastValue = newCityNames[len(newCityNames)-1];
print(lastValue); #notice the blank line after printing out "London"
newCityNames[len(newCityNames)-1] = lastValue[0:len(lastValue)-1]; #get rid of the \n at the end
print(newCityNames[len(newCityNames)-1]); #no blank line after "London"

print(newCityNames);
print("bbbbbbbbbbbbbbbbbbbbbbbbbbb\n");

#construct the new distance array
#keep reading lines, when the for loop ends, interator pointer will point to the end of the line, thus there is no more to read
for x in frd:
    newRow=x.split(',');
    newLastValue = newRow[len(newRow)-1];
    newRow[len(newRow)-1] = newLastValue[0:len(newLastValue)-1];
    newDistance.append(newRow);

print(newDistance);
#all values are read as a string type
#can further refine the array by converting all values into integers



#--------------------------------------------------------------------
#Working with directories
#-------------------------------------------------------------------
#sometimes you need to specify the directory(folder) where the file resides.
#The os module provide methods for working with files and directories

import os;

#get the current directory name (where this python file is)
cwd = os.getcwd();
print(cwd);

#check if a file exists
print(os.path.exists("distance.csv"));
print(os.path.exists("/home/linglu/PythonProgramming/week8/distance.csv"));
print('\n');

#check if it is a directory
print(os.path.isdir("distance.csv"));
print(os.path.isdir("/home/linglu/week9"));
print('\n\n');

#check if it is a file
print(os.path.isfile("distance.csv"));
print(os.path.isfile("/home/linglu/week9"));
print('\n');

#create a new directory
"""
path = os.path.join(os.getcwd(),"data2");
os.mkdir(path); #if the directory already exists, will generate a run time error
#create a file in the new directory
fw = open("data2/newFile.txt",'w');
fw.write("This is a test.");
fw.close();
"""


#-----------------------------
#exception handling
#-----------------------------
#Sometimes you don't have permission to write to a directory, or the file you are trying to read from doesn't exist
#The system will generate an error. You need to handle exceptions like this so the file runs to the end without generating an error.
#This will provide better user experience and prevent security breach.

#fr = open("badfile.txt",'r');
#The above line will generate an error, since the file doesn't exist
#To avoid this, you can handle the exceptions manually using methods such as exists(), isfile() etc.
#You can also use the built-in infrustructures as below.
#They are ofen called "Try and Catch" blocks, thus the term "Catch the exceptions".
try:
 fr = open("badfile.txt",'r');
 fr.read();
 #result = x / y; #another possibility that a run time error occurs

except: #if anything goes wrong during run time, the "except" block will be executed
    print("The system is experiencing technical difficulties. Please contact your system administrator or try again later. ");
    print("Bye!");



print("test");

#in some programming languages, the word "catch" instead of "except" is used

#in-class discussion, use the employee array and create a new directory for each employee, and put the rest of the employee information in a file under that direcotry
#e = [["John",30,"manager",55000],["Alex",25,"staff",35000],["Jane",35,"staff",48000],["Simone",28,"staff",50000]];




