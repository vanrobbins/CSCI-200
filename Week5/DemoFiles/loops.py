"""
File Name: loops.py
Purpose:
    This file introduces loops concepts, while loops and breaks
Variables used:
    (You need to have this section if this file is to solve a particular problem)
First Create Date: July 10, 2023
Last Update Date: July 20, 2024
Author: Lingma Lu
Version: 1.1
"""

#Sometimes a block of statements needs to run repeatedly for a number of times.
#This is called "iteration", commonly known as "loop".
#Often, the task is defined as "keep doing something until ...", for instance -
#keep asking for user username and password, until the correct ones are entered
#add all integers from 1 to 1000: keep adding the next integer until 1000 is added
#finding the average salary: keep adding salaries, until all are added, then devide the total sum by salary count
#print out all even numbers between 0 to 20: keep printing until 20 is printed
#when searching for a book in a database, keep looking until found or until all books have been scanned


#To define a loop, the following mechanism must be satisfied:
#1. choose a loop structure
#2. define when the repetition starts
#3. define how many times the block should be repated or when the repetition should stop
#4. define how to reach the stopping point
#5. define what statement block need to be repeated (most times with different values or expressions)

#Important: the looping must be controled in a way that the repetion will stop, otherwise, an infinite loop will happen.


#"while" loops
#define a condition after the keyword "while" (loop header), as long as the condition is true, keep running the loop body
#define a mechanism so that the condition will become false; if the condition never becomes false, an infinite loop occurs
#define the statement block (loop body)

#Example: Indy 500 lap counter - each car will run 200 laps, display the lap count for a particular car
#rephrase - keep printing the car number and the lap count, until the last lap is printed.
#start: 1, end: 200
#how to reach: increment by 1
#what is repeated: printing statements

car = "No. 8";
lap = 1;

while (lap <= 20):
    print(car);
    print("lap " + str(lap));
    print("Go Ed!");
    lap = lap +1; #increase the value by 1 so that it can get up to 200 to stop the loop


#Example: New Year's Even count down. What is the ouput of the following code block?
#keep printing the count down number until 0 is reached.
#start: 10, end: 0
#how to reach the stopping point: decrease by 1
#what is repeated: print out the number

count = 10;
while (count >=0):
    print(count);
    count = count - 1; #decrease the value so that the count can go own to 0 to stop the loop

#Example: What is the output of the following code block?
'''
count = 10;
while (count <= 10):
    print(count);
    count = count - 1;
'''

print("*************");
#Example: What is the output of the following code block?
count = 10;
while (count > 10):
    print(count);
    count = count - 1;
print("*************");

#Example: add up all integer values from 1 to 100.
#start: 1, end: 100
#how to reach the end point: increment by 1
#what is repeated: adding the next integer to the total sum

v = 1;
sum = 0;

while (v <= 100):
	sum = sum + v;
	v = v + 1;

print("=============== total sum is " + str(sum));

#Excercise: add up all even values from 1 to 100.
e = 1;
sum = 0;
# ...
# ...

print("**** sum of  all even numbers is " + str(sum));




#keyword "break" is used to jump out of the loop, before the termination condition is met
#Example: prompt user for a keyboard entry, until the user enter "done"
while True:
    line = input('next > ');
    if line == 'done':
        break;
    else:
	    save = save+","+line +","; #keep appending the user input and a comma
print(save);

print("------------------ final line is " + line);

#A modified version - remember the user entries
entry = "";
count = 0; #since the condition is always True, sometimes you need to use a variable to remember how many times the loop body is executed
while True:
    count = count + 1;
    line = input('next > ');
    if line == 'done':
        break;
    if (count == 1):
        entry = line;
        print("entry is " + entry);
    else: entry = entry + "," + line;
    print(entry);

print("------------------ final entry is " + entry + " and final count is " + str(count));

#Note: "break" will only break out of the enclosing loop
x = 0;
y = 0;

while (x <= 3):
    x = x + 1;
    print("----- x is " + str(x));
    y = 0;
    while (y <= 4):
        y = y + 1;
        print("y is " + str(y));
        if (y == 2):
            break;


print("!!!!!!!!!!!!!!!!!!!!");

#keyword "continue" is used to skip the remaining statements in the loop body and continue with the next iteration
#Example: add the even numbers in the 1 - 10 sequence
count = 0;
sum = 0;
while True:
    count = count + 1;
    if (count == 10):
        break;
    if (count%2 == 1):
        continue;

    sum = sum + count;
    print("count is " + str(count));


print("Final sum is " + str(sum));


#in-class exercise, use pseudocodes to give the algorithm for the following problem:
#ask the user to enter a salary from keyboard, and compute the average of all the values
#if an invalid value is entered such as a non-numeric value or a negative value, inform the user and ask to enter again
#otherwise, move forward to compute the average, and output the final average salary
#make sure your algorithm is correct before you submit. Do not check your algorithm through writing codes.
