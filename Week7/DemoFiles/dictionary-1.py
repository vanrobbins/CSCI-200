"""
File name: dictionary.py
Purpose: This file demonstrate the dictionary data type.
Author: Lingma Lu
Create date: 07/13/2023
Last update date:02/27/2024
version: 1.1
"""

#A dictionary is similar to a list, except that the values are identified by a label (usually a value of string type), rather than a numerical index.
#The elements in a dictionary are key-value pairs (a key maps to a value)

"""
''''''''''''''''''''''''''''
Creating the structure
'''''''''''''''''''''''''''
"""
#Create a dictionary method 1: use the dict() function to create an empty structure, then add data using []
#create a dictionary to store employees' strongest programming skills
skills = dict();

skills["John"] = "Python"; #key-value pair: "John"-"Python"
print(skills);

skills["Alex"] = "C"; #key-value pair: "Alex"-"C"
print(skills);

skills["Jane"] = "Python";
print(skills);

skills["Simone"] = "Java";
print(skills);

skills["Simone"] = "C++"; #will not add the same key twice, value will be updated. Thus keys must be unique.
print(skills);

print(len(skills)); # length is 4. The structure has 4 pairs of data

print("******************************\n");

#A key must be text or numeric type, a value can be any type (string, int, float, boolean)
evaluation = dict();
evaluation["1"] = True;
evaluation["2"] = True;
evaluation["3"] = False;
print(evaluation);

#although the followings are allowed, avoid using integers as keys as they will look like array indices
evaluation[1] = True;
evaluation[2] = True;

print(evaluation);

print("-------------------------------\n");


#Create a dictionary method 2: use {} and add key-value pairs inside the {}
temperature = {"Indianapolis":80,"Chicago":84,"Fort Wayne":79};
print(temperature);

keypad = {'a':2, 'b':2, 'c':2,'d':3,'e':3,'f':3};
print(keypad);

#can use variables to specify keys and values, if certain values need to be repeated
x = 2;
y = 3;
keypad = {'a':x, 'b':x, 'c':x,'d':y,'e':y,'f':y};
print(keypad);

keypad2 = {x:x, x:x, y:y, y:y}; #can be used to initialize a structure with default values
print(keypad2);

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");

#Create a dictionary method 3: use the dict() function and add data as function inputs
employee = dict(Name = "John", Age = 36, Branch = "Norway"); #note: keys cannot be in quotes when using method 3
print(employee);

#create a nested structure using combination of method 2 and method 3
#employess is a dictionary of 2 key-value pairs; for pair 1, key is E1 and value is a dictionary of 3 key-value pairs
employees = dict(
    E1 = {"Name":"John Mann", "Age":36, "Branch":"Norway"},
    E2 = {"Name":"Mary Hopkins", "Age":25, "Branch":"France"}
    );
print(employees);

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n");


#use a loop to add keys and values
s = "abcdef";
d = dict();
i = 0;
for k in s: #retrieve a character in the string s, store it in variable k
    d[k] = i; #e.g. d['a'] = 0 in the first iteration
    i = i + 1;

print(d);

print("\n");

"""
''''''''''''''''''''''''''''''''''''''''''''''''''''
updating the structure
''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
temperature = {"Indianapolis":80,"Chicago":84,"Fort Wayne":79};

temperature["Indianapolis"] = 90; #this will change a value to the key
print(temperature);

temperature.update({"Detroit":90}); #this will add a new pair since there is no key named "Detroit"
print(temperature);

temperature.update({"Detroit":80}); #this will change the value of key "Detroit" since this key exists
print(temperature);


temperature.pop("Detroit"); #this will remove the key-value pair
print(temperature);

d.clear(); #this will empty the structure
print(d); #can print since the structure still exists

del d; #this will delete the structure, can be used when you no longer need the structure to release memory space
#print(d) #this will generate an error since the structure no longer exists

print("ooooooooooooooooooooooooooooooooooooooooooooooo\n");



"""
''''''''''''''''''''''''''''
retrieving values
'''''''''''''''''''''''''''
"""
#a value is retrieved using the key
print(temperature["Indianapolis"]);
print(keypad2[2]); #2 is a key, not an array index
#cannot retrieve a value through an index
#print(keypad2[0]); #identify 0 as a key, thus will generate an error

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n");

#print out the mapping for sequence aaeb
keypad = {'a':2, 'b':2, 'c':2,'d':3,'e':3,'f':3};
print(keypad['a']+keypad['a']+keypad['e']+keypad['b']); #since the values are integers, math operation is performed
print(str(keypad['a'])+str(keypad['a'])+str(keypad['e'])+str(keypad['b'])); #this is the desired result
#tip: define the value to be text type if no math will be involved with the values

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n");


#check if a key exists
print("Indianapolis" in temperature);

city = "Indianapolis";
if (city in temperature):
    print("Temperature of " + city + " is " + str(temperature[city]));

#print out all the keys
print("temperature keys: {} ".format(temperature.keys()));

#print out all the values
print("temperature values: {} ".format(temperature.values()));


#check if a value exists
t = 90;
if (t in temperature.values()):
     print("There is a city with temperature " + str(t));

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n");

#use for loop to access each key:value pair
#find the average temperature
totalTem = 0;
for k in temperature: #get each key and store in variable k
    #print(k + "->" + str(temperature[k])); #print out the key and the value for that key
    totalTem = totalTem + temperature[k];

print("Average temperature is " + str(totalTem/len(temperature)));

print("++++++++++++++++++++++++++++++++++++++++++++++\n");


#use for loop to access each key:value pair in a nested dictionary
del employees;
employees = dict(
    E1 = {"Name":"John Mann", "Age":36, "Branch":"Norway"},
    E2 = {"Name":"Mary Hopkins", "Age":25, "Branch":"France"}
    );
print(employees);

#find information for Mary Hopkins
n = "Mary Hopkins";
for i in employees:#get each key and store in variable i
    print("i is " + str(i));
    e = employees[i]; #get the value for the key, and store it in variable e, thus e is a dictionary structure
    if (e["Name"] == n): #get the value for key "Name" in the nested dictionary
        for j in e: #loop through each element of this employee
          print(j + "->" + str(e[j])); #print out the key and the value for that key


#in-class exercise: there is no built-in function or method to find the key based on a value, since there may be more than one keys mapped to that value.
#how to write a function find the key(s) based on a given value? Use "temperature" to implement.