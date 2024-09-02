"""
File Name: commentingAndDebugging.py
Purpose:
    This file illustrates the use of variables and expressions.
    It is the solution for the problem below:
    "Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
     $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?"
Special Requirement: all values used must be first stored in variables
Variables created in the file, in the order of creation:
    coverPrice:  cover price for the book
    discount: discount the bookstore can receive
    firstShippingCost: price for shipping the first book
    firstShipping: number of books to pay at a high shipping rate
    additionalShippingCost: lowered shipping cost for additional copies
    additionalCopy: number of books to pay at the lower shipping cost
    discountPrice: discounted price for the book store
    totalCopy: total number of books ordered
    totalCost: final cost for purchasing all the books including shipping
    message: final message to print out the result
First Create Date: July 1, 2023
Last Update Date: 08/29, 2023
Author: Lingma Lu
Version: 2.1
"""

#Create variables and initiate values
coverPrice = 24.95; #cover price for the book
discount = 0.4; #discount the bookstore can receive
firstShippingCost = 3; #price for shipping the first book
firstShippingCopy  = 1; #number of books to pay at a high shipping rate
additionalShippingCost = 0.75; #lowered shipping cost for additional copies
additionalCopy = 0; #number of books to pay at the lower shipping cost, initiated to 0 and calculated later
discountPrice = 0.0; #discounted price for the book store, initiated to 0.0 and calculated later
totalCopy = 60; #total number of books ordered
totalShippingCost = 0; #cost for shipping only
totalBookCost = 0;  #cost for books only
totalFinalCost = 0.0; #final cost for purchasing all the books including shipping, initiated to 0.0 and calcuated later
message = ""; #final message to print out the result, initiated as an empty string

#Find the additional copies
additionalCopy = totalCopy - firstShippingCopy;
print("aaaaa additionalCopy is "  + str(additionalCopy));

#Syntax error: grammatical mistake
#print("aaaaa additionalCopy is"  str(additionalCopy));


#run time error: no grammar mistake but error encountered when program runs
#print("aaaaa additionalCopy is" + additionalCopy);


#another example of run time error:
a = 2; b = 0;
#print("00000 a divide by b is " + str(a/b));

#Find the discount
discountPrice = coverPrice * discount;
print("bbbb discount Price is " + str(discountPrice));

#calculate the total cost
totalShippingCost = firstShippingCost * firstShippingCopy + additionalCopy * additionalShippingCost;
print("ccccc total shipping cost is " + str(totalShippingCost));

totalBookCost = round(totalCopy * discountPrice, 2);
#The round() function returns a floating point number that is a rounded version of the specified number(first input), with the specified number of decimals(second input).
print("ddddd total book cost is " + str(totalBookCost));

TotalFinalCost = round(totalShippingCost + totalBookCost, 2);
print("eeeee total final cost  is " + str(TotalFinalCost));

#totalFinalcost = totalShippingCost * totalBookCost;
#print("fffff total final cost  is " + str(totalFinalcost));
#logic error: program runs successfully but generated incorrect result

message = "The final cost is $" + str(totalFinalCost) + "!";
#logic error: program runs successfully but generated incorrect result
print(message);


"""
Summary of good coding practice:
1. Have a file header that includes but is not limited to file name, purpose of the file, author, first create date, last update date, version number.
Other items can include related files, purpose of the variables created, special notes.
2. Organize codes into blocks and each block has its own purpose, e.g. a block to create variables and initiate values, a block to calculate a certain value, a block for output
3. Create variables with meaningful names and do not create variables with similar names
4. Following a certain convention when naming variables, functions, files
5. Leave comments whenever necessary using block comments or single line comments
6. Avoid hard coding
7. Do not create a variable that will not be used later

"""


