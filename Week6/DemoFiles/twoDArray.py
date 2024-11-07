"""
File name: twoDArray.py
Purpose: This file demonstrate the application of a 2-D list.
Task: find the distance between two cities using a given distance chart
Author: Lingma Lu
Create date: 07/13/2023
Last update date:07/27/2024
version: 1.2
"""

#Elements of a list can be lists

'''
Example: create a matrix structure with 3 rows and 4 columns, as below
1   2   3   4
5   6   7   8
9   10  11  12

'''
a = [[1,2,3,4],[5,6,7, 8],[9,10,11,12]];

print("a is {}".format(a));
print(a[0]); #print out first row
print(a[0][0]); #print out value at first row first column
print(a[2][3]); #print out value at third row fourth column

#create a 2-D array with 2 rows and 3 columns and initialize the values to a random integer
import random;

newList = []; #create an empty list
i = 0;
row = 2;
j = 0;
column = 3;

for i in range(row):
    newRow = []; #in each iteration, create a new row whose values will be populated by the inner for loop
    for j in range(column):
        newRow.append(random.randint(0,100));

    newList.append(newRow);

print("\nThe new list is {}\n".format(newList));

#print out values using loops
for i in range(row):
    newRow = newList[i]; #get a row and assigned the row values to newRow
    for j in range(column):
        print(newRow[j]);
    print("------------");

print("\n");
#another version
for i in range(row):
    for j in range(column):
        print(newList[i][j]);

    print("++++++++++");

print("\n\n");


#Application: use a distance chart, ask the user to enter two cities and display the distance between two cities

#prepare the distance chart
cityNames = ["Indianapolis", "New York", "Tokyo", "London"];
distanceChart = [[0, 648, 6476, 4000],[648, 0, 6760, 3470],[6476, 6760, 0, 5956],[4000, 3470, 5956, 0]];

#Take user inputs for city choices
#For simplicity purpose, city choices are hard-coded here. Normally it will come from user inputs and input validations are performed.
cityA = 0;
cityB = 1;

result = distanceChart[cityA][cityB];

print("The distance between {} and {} is {} miles.".format(cityNames[cityA], cityNames[cityB], result));


#in-class discussion: how to turn this structure into a 2-D array and find the average age and total salary
e = "John,30,manager,55000;Alex,25,staff,35000;Jane,35,staff,48000;Simone,28,staff,50000";

