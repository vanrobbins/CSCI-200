"""
File Name: string.py
Purpose:
    This file introduces string operations and for loops
First Create Date: July 10, 2023
Last Update Date: July 23, 2024
Author: Lingma Lu
Version: 1.2
"""


#String Operations
#A string is a sequence of alpha-numeric characters
#You can access a particular character by using the [] and an index to indicate the position
fruit = "passion fruit"; #what is the length of this string?
firstLetter = fruit[0]; #index value 0 refers the first element in the sequence
print("First letter is " + firstLetter);
print("Third letter is " + fruit[2]);
i = 3;
print("Another letter is " + fruit[i+1]);
print("Another letter is " + fruit[i+5]);
#what is the output of the line below? What type of error is it (syntax, run-time, logic)?
#print("Another letter is " + fruit[i+10]); run-time

print("\n");

#Certain built-in functions can be used on strings - https://www.w3schools.com/python/python_ref_functions.asp
#finding the length of a string
print("Length of the string fruit is " + str(len(fruit))); #a white space is a character
print("The last character of the string fruit is " + fruit[len(fruit)-1]);
#or use negative index
print("The last character of the string fruit is " + fruit[-1]);

test = "test\n";
print("Length of the string test is " + str(len(test))); #new line character is one character

print("*********************\n");

#since we know the length of the string, we can use a while loop to traverse the string
print("Traverse the string fruit:\n");
index = 0;
while (index < len(fruit)):
    letter = fruit[index];
    print(letter);
    index = index + 1;




#use a "for" loop to traverse a string
for n in fruit: #for every element in the string fruit, store it in variable n, n is a new variable
    print("in for loop " + n);



print("n is " + str(n)); #when loop ends, n's value is the last character of the string

print("--------------------\n");

#string slices
fruit = "passion fruit";
piece = fruit[0:5]; #starting from 0th character to the 4th character, take the first 5 characters
print("piece is " + piece);


print("first 6: " + fruit[:6]); #omit the first index, slice starts from the beginning of the string
print("character #8 to end:__ " + fruit[7:]); #omit the second index, slice starts goes to the end of the string
print("no index: " + fruit[:]); #entire string
print("same index: " + fruit[3:3]); #no character can be found


print("ooooooooooooooooooooo\n");

#strings are immutable, which means once a string is created, its value cannot be changed.
#if you need to change a string value, you should create a new string

name = "Carl";
newName = "K" + name[1:];
print("New name is " + newName);

#application: search for a particular character in a string
#find the first index of the "letter" in the given "word"
#return the index of the letter, or -1 if not found
def find(word, letter):
    index = 0;
    while (index < len(word)):
        if (word[index]) == letter:
            return index; #once a function return a value, the execution stops
        index = index + 1;

    return -1; #return a special value (different from any other returned values) to indicate a special result


searchResult = find(fruit, "i");
if (searchResult == -1): print("Letter not found in string.");
else: print("Letter found in position " + str(searchResult + 1));

searchResult = find(fruit, "s");
if (searchResult == -1): print("Letter not found in string.");
else: print("Letter found in position " + str(searchResult + 1l));


print("aaaaaaaaaaaaaaaaaaaaaaa\n");

#string methods are similar to functions, but use a different syntax
#will talk more about the difference between methods and functions later
#https://www.w3schools.com/python/python_ref_string.asp
#https://docs.python.org/3/library/stdtypes.html#string-methods

print("Turn to upper case: " + fruit.upper()); #turn the string to upper case, use a built-in string method. This does not change the string value
print("value of fruit is still: " + fruit);

#if you need to keep the upper case verson of the string, need to store it to a variable
upperFruit = fruit.upper();
print("Upper case of the fruit value: " + upperFruit);


#string values are case sensitive, sometimes you can change all characters to the same case before comparing values
#E.g. when finding the book whose title contains the word "database", if a title is "Fundamental Database Concepts", if you do not turn the title into all lower case, this book will not be found.

searchResult = fruit.find("ra"); #another built-in string method, first the first occurence of a charact or a string, similar to the user-defined function above, but can find a substring
if (searchResult == -1): print("Letter not found in string.");
else: print("Letter found in position xxxxx " + str(searchResult + 1));

print("\nNameeeeeeeeeeeeeeeeeeee");
#application - split a person's full name into first name and last name
#algorithm: find the index of the first white space, then use this index to find the first name and last name
name = "John Smith";
firstName = "";
lastName = "";
whiteSpaceIndex = name.find(" ");
if (whiteSpaceIndex == -1): print("Invalid name format");
else:
    firstName = name[0:whiteSpaceIndex];
    lastName = name[whiteSpaceIndex + 1:];

print("First name is: " + firstName + " and last name is: " + lastName);

#Question for you - how to split a person's full name into first name, middle name (if there is a middle name, or if there are more than one middle names) and last name


#find the character in an index range, passion fruit
searchResult = fruit.find("a", 0, fruit.find(" ")); #find the character from the beginning till the index of the white space, i.e. find the letter a in the first word
if (searchResult == -1): print("Letter not found in the first word.");
else: print("yyyyyyyyyyy letter a found in position " + str(searchResult + 1));



#"in" operator takes two strings and returns TRUE if the first appears in the second
print("contain passion? " + str("passion " in fruit));
print("contain apple? " + str("apple" in fruit));


#Question for you - how to split a person's full name into first name, middle name (if there is a middle name, or if there are more than one middle names) and last name
#algorithm:
"""
a. get the firts index of space, use it to get the first name;
b. get the last index of the space, use it to get the last name; Q: how to get the last occurence of a character?
c. if the first index is the same as the last index, done, else -
        slice out everything from the first and last index,  and store in a new string ns
        process ns: keep looking for white space, when one is found, store the index, get the part before the index, append it to the mn string, slice out the substring from the index to the end, store in a new string,  until done

"""


'''
find first occurence of space
assign first name to be the sliced string from index 0 to index of first occurence space
find last occurence of space
assign last name to be the sliced string from last occurence of space index to end of string index
assign middle names to equal sliced string from first occurence of space index to last occurence of space index
    use loop to find middle names until does not find space
        find occurence of space 
            assign middle name[x] to slice string from beginning of string to first occurence of string
            slice string from space to end of string index
            x+1 so middle name is saved to own variable
'''



