"""
File name: badCoding.py
Purpose: This file shows some bad examples of coding.Bad coding includes but is not limited to the following:
1.create a variable but never use it
2.function returns a value but the return value is not used
3.print program specific message in a function
4.variable name not showing the purpose
5.function name not showing the purpose
6.change a global value or a structure through pass-by-reference method inside a function when not necessary
7.use a global variable where a local variable can be used
8.not create a function when should
9.create a function that does many different tasks
10.reuse a variable when a new one should be created
11.create a new variable when the same one should be used
12.not following a naming convention
13.not consider user behaviors, e.g. not verifying user input before processing inputs, assuming user will enter a value as required
14.not consider the fact that the array size may grow, e.g. harding an array size instead of using the length function
15.not use a utility file when should
16.executable codes not grouped together (normally, function definitions are grouped together, and executable lines are grouped together)
17.create a variabe of inapproproate type, e.g. zipcodes should be of string type
18.function returns an improper value or returns a global variable
19.hard coding when shouldn't
20.output not correctly formated
21.use integers in a dictionary that look like indexes
22. not initializing key variables at the beginning of a file

Author: Lingma Lu
Create date: 10/17/2023
Last update date:3/10/2024
version: 1.1
"""

#A dictionary is similar to a list, except that the values are identified by a text, rather than a numerical index.
#The elements in a dictionary are key-value pairs (a key maps to a value)

"""
''''''''''''''''''''''''''''
Creating the structure
'''''''''''''''''''''''''''
"""
#Create a dictionary method 1: use the dict() function to create an empty structure, then add data
#create a dictionary to store employees' strongest programming skills
skills = dict();

skills["John"] = "Python"; #key:value pair: "John":"Python"
print(skills);

skills["Alex"] = "C"; #key:value pair: "Alex":"C"
print(skills);

skills["Jane"] = "Python";
print(skills);

skills["Simone"] = "Java";
print(skills);

skills["Simone"] = "Java"; #will not add the same key twice, statement is ignored
print(skills);

print(len(skills)); # length is 4. The structure has 4 pairs of data

print("******************************\n");

#bad #1: create a variable but never use it
#bad #17: create a variabe of inapproproate type
#create a salary dictionary to store employee salary
salary = dict();
salary2 = dict();

salary["John"] = "65029"; #salary values should be numeric to facilitate mathematical computations
salary["Alex"] = "40876";
salary["Jane"] = "33560";
salary["Simone"] = "77840";
print("===============================\n");

#bad #5:function name not showing the purpose
def fs(skillList, name):
    #bad #3: print program specific message in a function
    #bad #19: hard coding when shouldn't
    #bad #20: output not correctly formated
	print("Bad coding example - Alex's skill is " + skillList[name]);
	return skillList[name];

fs(skills, "Alex"); #bad #2: function returns a value but the return value is not used

fs(skills, "Simone");

print("aaaaaaaaa\n");

def findSkill(skillList, name):
	return skillList[name];

name = "Alex";
#name = "Simone";
skillFound = findSkill(skills, name) ;
print(name + "'s skill is " + skillFound + ".");

print("bbbbbbbbbb\n");

#bad #6:change a global value or a structure through pass-by-reference method inside a function when not necessary
#bad #9:create a function but shouldn't
print(skills);
def changeSkill(skillList, name): #a dictionary structure is also passed into a function using pass-by-reference method
    skillList[name] = "C,Java";

changeSkill(skills, "Alex");
print(skills);

#a better alternative
skills["Alex"] = "C,Java";
print(skills);

#bad #7: use a global variable where a local variable can be used
name = "Alex";
def changeSkillBad7(skillList): #a dictionary structure is also passed into a function using pass-by-reference method
    global name;
    skillList[name] = "C,Java,Python";
    return name; #bad #18:function returns an improper value or returns a global variable

changeSkillBad7(skills); #bad #2: function returns a value but the return value is not used
print(skills);

print("cccccccccccccccccccc\n");

"""
13.not consider user behaviors, e.g. not verifying user input before processing inputs, assuming user will enter a value as required
14.not consider the fact that the array size may grow, e.g. harding an array size instead of using the length function
15.not use a utility file when should
16.executable codes not grouped together (normally, function definitions are grouped together, and executable lines are grouped together)
17.create a variabe of inapproproate type, e.g. zipcodes should be of string type
18.function returns an improper value or returns a global variable
19.hard coding when shouldn't
20.output not correctly formated
21.use integers in a dictionary that look like indexes
22. not initializing key variables at the beginning of a file
"""
