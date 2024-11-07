"""
File Name: passByReference.py
Purpose:
    This file demonstrates pass-by-value and pass-by-reference
First Create Date: July 13, 2023
Last Update Date: July 27, 2024
Author: Lingma Lu
Version: 1.1
"""


#rewrite the distance chart problem by creating a function

cityNames = ["Indianapolis", "New York", "Tokyo", "London"];
distanceChart = [[0, 648, 6476, 4000],[648, 0, 6760, 3470],[6476, 6760, 0, 5956],[4000, 3470, 5956, 0]];

def findDistance(fromCity, toCity, distanceArray):
    result = distanceArray[fromCity][toCity];
    return result;

cityAIndex = 1; #for simplicity purpose, choice is hard-coded here. It should come from user input and invalid entries should be checked
cityBIndex = 3;
distance = findDistance(cityAIndex, cityBIndex, distanceChart);
print("The distance between {} and {} is {}".format(cityNames[cityAIndex], cityNames[cityBIndex], distance));

cityAIndex = 0;
cityBIndex = 2;
distance = findDistance(cityAIndex, cityBIndex, distanceChart);
print("The distance between {} and {} is {}".format(cityNames[cityAIndex], cityNames[cityBIndex], distance));



#pass-by-value: when an argument value is passed into a function, its value is stored in a new local variable(parameter), e.g. fromCity, toCity  in line 17 are two new local variables.
#pass-by-reference: when an argument value is passed into a function, a local reference variable(parameter) is created and points to the memory location of the orginal variable.
#when a list is passed into a function, it uses pass-by-reference method.
#The value of the reference variable is the memory address of the first element in the list.
#distanceChart and distanceArray point to the same memory space storing those array elements.
#If pass-by-value, changing the value of the new local variable will not change the value of the argument variable
#If pass-by-reference, changing the value of the local reference variable will change the value of the argument, since they point to the same memory space
def turnToFloat(twoDList):
    i = 0;
    j = 0;
    for i in range(len(twoDList)):
        rowLength = len(twoDList[i]);
        for j in range(rowLength):
            twoDList[i][j] = float(twoDList[i][j]); #values of the argument are changed to float type


def findAndModifyDistance(fromIndex,fromName, toIndex,toName, distanceArray): #distanceArray is a reference variable
    distance = distanceArray[fromIndex][toIndex];
    fromName = fromName + " City"; #local variable value is changed for more clarity
    toName = toName + " City";
    turnToFloat(distanceArray);
    result = "The distance between {} and {} is {}".format(fromName, toName, distance);
    return result;

#call the function
cityAName = cityNames[cityAIndex];
cityBName = cityNames[cityBIndex];
message = findAndModifyDistance(cityAIndex,cityAName, cityBIndex,cityBName, distanceChart); #distanceChart is passed into the function using pass-by-reference method
print(message);


print("new city name? No. {}".format(cityAName));#original cityName is not changed

print("new distance? Yes. {}".format(distanceChart));  #original list values are changed to floats inside the function turnToFloat()


