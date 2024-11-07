"""
File Name: list.py
Purpose:
    This file demonstrates list operations
First Create Date: July 13, 2023
Last Update Date: July 27, 2024
Author: Lingma Lu
Version: 1.2
"""


#A list is a type of object(variable) that stores a sequence of values, of the same or different types
#A common name is "array", and different languages has varied concepts and syntax, e.g. C language only allows arrays of same type of values while Python can use a list to store different types of values
#The values in a list is called elements or items

#create a list of names
names = ["John Smith","Alex Hoover","Jane Fonda","Simone Raddle"]; #list elements are of string type
print(names);
#print("Employee names are " + names); #This line will generate an error since names is not a str type of variable.
print("Employee names are " + str(names));

#create a list of ages
ages = [30, 25, 35, 28]; #list elements are of integer type
print(ages);

#create a list of job ranks
ranks = ["F-2", "F-5", "P-1", "P-3", "F-2"];
print(ranks);

#We can use the above three lists to hold employee information, and same index in each list refers to information about the same employee.
#Use index to access elements, index values starts from 0.
print("\nInformation for the first employee:\nName: " + names[0] + ", Age: " + str(ages[0]) + ", Rank: " + ranks[0]);
#another way to format the output
print("\nInformation for the second employee: {},{},{}".format(names[1], ages[1], ranks[1])); #formats the specified value(s) and insert them inside the string's placeholder.
print("\nInformation for the third employee: {1}, {0}, {2}!".format(names[2], ages[2], ranks[2])); #insert according to the positions of the values in the format() argument list
#more on the method format() - https://www.w3schools.com/python/ref_string_format.asp

#lists are mutable, use index to change its values
names[0] = "John A Smith";
print(names);
#names[4] = "Sam"; #generates an error
#print(names);
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx");


#use a loop to populate a list

import random;

salary=[]; #create an empty list, elements will be added later. This line symply announces salary is a list type of variable.
i = 0;
while (i < len(names)): #use length of names to dynamically find the length, do not hard code to 3
    #since salary is an empty list, we first increase the size (use the append() method and giving 0 as initial value so that the variable can exist (get a space in memory)
    salary.append(0); #must append one value to generate the list
    salary[i] = random.randint(10000,80000); #change the value in each iteration, use the random number generator
    print("salary {} is {}".format(i, salary[i]));
    i = i + 1;

print(i);
print(salary);
print("Total Salary is: " + str(sum(salary))); #use built-in function to get the sum of list values
print("Average Salary is: " + str(sum(salary)/len(salary))); #there is no built-in function for the average

#another version to populate an empty list - use append only
salary=[]; #create an empty list, elements will be added later
i = 0;
while (i < len(names)): #use length of names to dynamically find the length, do not hard code to 3
    #use append only
    salary.append(random.randint(10000,80000));
    print("salary {} is {}".format(i, salary[i]));
    i = i + 1;

print(i);
print(salary);
print("Version 2: Total Salary is: " + str(sum(salary)));
print("Version 2: Average Salary is: " + str(sum(salary)/len(salary))); #there is no built-in function for the average


print("\n==================================");

#change the salary into a different currency and store in a new list
salaryInEuro = [];
i = 0;

while (i < len(salary)):
    salaryInEuro.append(0);
    salaryInEuro[i] = salary[i]*0.89;
    print("while loop, salary in dollar: {}, salary in Euro {:.2f}".format(salary[i], salaryInEuro[i])); #format into floating point number with 2 digits after the decimal point
    i = i + 1;


#rewrite the above using a for loop
#Most of the times, you can use a while loop and for loop structure interchangeably, but there are times you cannot rewrite a while loop using a for loop structure since while loop requires a condition and for loop doesn't.
salaryInEuro = []; #reset it to empty
i = 0;

for v in salary: #for each element in the salary array, store the value into variable v
    salaryInEuro.append(0);
    salaryInEuro[i] = v*0.89;
    print("for loop, salary in dollar: {}, salary in Euro {:.2f}".format(v, salaryInEuro[i])); #format into floating point number with 2 digits after the decimal point
    i = i + 1;



#another version
salaryInEuro = []; #reset it to empty
i = 0;

for i in range(len(salary)): #for each value in range 0 - 3, store the value in i; range(n) returns a list of indices from 0 to n - 1, in this example, n is the length of the salary list.
    salaryInEuro.append(0);
    salaryInEuro[i] = salary[i]*0.89;
    print("for loop2,  salary in dollar: {}, salary in Euro {:.2f}".format(salary[i], salaryInEuro[i])); #format into floating point number with 2 digits after the decimal point


print("==================================\n\n");

#Question: how to generate a list of 1000 random integers between 1 and 100, using a for loop?


#-----------------------------------------------------------
#list operators
#-----------------------------------------------------------
#"in", returns true if the value before the keyword is in the list
#What are the output of the following lines?
print(names);
print("Is John A Smith in the list? " + str("John A Smith" in names));
print("Is John A Smith in the list? " + "John A Smith" in names);
print("Is John Smith in the list? " + "John Smith" in names);


#"+", concatenate lists
#What is the output of this line?
a = [1,2,3,4];
b = [5,6,7,8];
print("a + b is {}".format(a+b));


#"*", repeats a given number of times
#What is the output of this line?
print("a*3 is {}".format(a*3));

#":", slice operator
#What is the output of this line?
print("a is {}".format(a[1:3]));

#change values in a list
print("b is {}".format(b));
b[1:3] = [10,11];
print("now b is {}".format(b));

print("\n\n0000000000000000000000000000000000");
#"is", returns true if two lists refer to the same object
a = [1,2,3];
b = a; #lists are objects, when you assign one object to another, both objects point to the same memory space
print("is b the same as a? {}".format(b is a));

c = [1,2,3];
print("Is c the same as a? {}".format(c is a)); #a and c are two different objects, even if their values are the same
#since a and b point to the same memory space, changes made to one object will affect the other object
print("b[2] is {} ".format(b[2]));
a[2] = 4; #a[2] is changed, however, b[2] is also changed
print("now b[2] is {} ".format(b[2]));

print("\n\n^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_");

#note: strings are immutable, but lists are
a = "123";
#a[2] = "e"; #cannot change a letter since a is created as a string, not a list
#if a is created as a list, its elements can be changed
a = [1,2,3];
a[2] = 9;
print("a is {}\n\n".format(a));

print("About del......................");
#"del", delete an element specified by an index or a range, length of list is changed
a = [1,2,3,4,5];
print("length of a is {} ".format(len(a)));
del a[1];
print(a);
print("now length of a is {} ".format(len(a)));

a = [1,2,3,4,5,6];
print("length of new a is {} ".format(len(a)));
del a[1:3]; #can delete a slice
print(a);
print("now length of new a is {} ".format(len(a)));



#--------------------------------------------------------------
#list methods
#--------------------------------------------------------------

print("\n\nList methods ........................");

t1 = ['a', 'b', 'c'];
t1.append('d');
print("t1 is {} ".format(t1));

t2 = ['h', 'e'];
t1.extend(t2); #add the argument to itself
print("new t1 is {} ".format(t1));

#use the string method .join() to connect the values in a list into a string, when a list is passed as an argument
#since join() is a string method, must start with a string, thus '' is used.
print("Joined t1 is " + ''.join(t1));
print(type(t1)); #t1 is still a list, values are not changed.
print(t1);
t1 = ','.join(t1); #t1 is a new variable of string type, comma serves as a connector for each element
print(type(t1));
print("new t1 is " + t1);

s = "abcde";
seperator = "***";
print("\nnew string is {} ".format(seperator.join(s))); #when a string is passed into join(), it is split by the specified character(s)


print("\n\nt2 sorted:");
t2.sort(); #t2 is updated to a list of sorted values
print("t2 is sorted as {}".format(t2));

#sort() changes the values of its caller and returns None when finished, thus the following will not create a new list t4
t3 = ['e','a','b'];
t4 = t3.sort();
print("\nt3 is {} ".format(t3));
print("t4 is {} ".format(t4));


print("\n\nAbout pop ...............................");
#pop() deletes an element at the given index value
t = ['a','b','c'];
t.pop(1);
print("\nt is {} ".format(t));

x = t.pop(1); #pop() return the element that was removed
print("x is {}".format(x));
print("\nnow t is {} ".format(t));

t = ['a','b','c'];
t.pop(); #if no index is provided, it removes the last element
print("\nAfter pop(), t is {} ".format(t));


#remove() specifies the actual value to be removed
t = ['a','b','c'];
t.remove('b'); #if no index is provided, it removes the last element
print("\nAfter remove(b), t is {} ".format(t));


print("\n\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv");

#-------------------------------------------------------------------
#list and strings
#-------------------------------------------------------------------

#list() function turns a string into a list
s = "spam";
t = list(s);
print("\ns is {} ".format(s));
print("t is {} ".format(t));


#split() method breaks a string into a list based on a specified delimeter
s = "John 30 manager 25000";
info = s.split(); #use the default delimer - blank space
print("Info is type {}, and values are {}".format(type(info), info));

s = "John,30,manager,25000";
info = s.split(","); #use "," as a delimeter
print("New Info is type {}, and values are {}".format(type(info), info)); #note: all values in the list are of string type, thus need to turn a value into integer type (such as salary) before using it



#create a list with different types
person1 = ["John Smith", 30, "manager", ["Python", "Java"]];
print(person1[3][0]);



#how to traverse this structure and find the average age and total salary
e = "John,30,manager,55000;Alex,25,staff,35000;Jane,35,staff,48000;Simone,28,staff,50000";


