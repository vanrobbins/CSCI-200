"""
File Name: lab7MentalHealth
Purpose:
Take Data from a csv file and copy it into another csv file with an extra colum
Takes report on weekly anxiety and depression in America based on location, race, etc. 
and adds median value from Quartile range

Special Requirements: 
Dataset must have at least 100 rows and 5 columns.
Exceptions are handled correctly.
-10 for each bad coding occurrence

First Created: 11/1/2024
Last Updated: 11/5/2024
Author: Van Robbins
Version 1.0
"""
import lab7Utility;
import datetime;

#Empty array that will hold csv data
newAnxietyDepression = [];
#Try to open main dataset
try:
    dataSet= open("anxietyDepression7Days.csv", 'r')
except:
    #If cannot quit
    print("The system is experiencing technical difficulties")
    quit();

for i in dataSet:
    #Stores line data in newLine array
    newLine=i.split(',');
    lastValue= newLine[len(newLine)-1];
    #Removes /n from last value
    newLine[len(newLine)-1] = lastValue[0:len(lastValue)-1];
    #Adds line to main array
    newAnxietyDepression.append(newLine);
dataSet.close();

#Resets i to 0 for next loop
i=0;
#Creates New csv file
newFile = open("anxietyDepressionWMedian.csv",'w')
#File Header
newFile.write("National Anxiety & Depression 7 Day Reports With Median\n")

while (i<len(newAnxietyDepression)):
    oneRow = newAnxietyDepression[i];
    j=0;
    while (j<len(oneRow)):
        oneValue = newAnxietyDepression[i][j]
        #If at end of row write last value and median or median header
        if (j ==(len(oneRow)-1)):
            newFile.write(str(oneValue)+',');
            if (i==0):
                #Adds Median Header Too End of Headers
                newFile.write("Median\n");
            else:
                #Finds Median given Quartile Range and adds to Median Colum
                newFile.write(str(lab7Utility.median(oneValue,"-"))+'\n');
        else: 
            newFile.write(str(oneValue)+',');
        j+=1;
    i+=1;
#File Footer
newFile.write("Author: Van Robbins; Date: "+ str(datetime.date.today())+";");

print("Done!")
