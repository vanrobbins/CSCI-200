"""
File name: VariablesInClass09032024
Purpose: Complete in class assignments for September 3rd 2024
    Activity 1: The Volume of a Sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with a radius of 5
    Activity 2: Suppose the cover price of a book is $24.95, but the bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents
                for additional copies. What is the wholesale price of 60 copies.
    Requirements: 
        All values used must first be stored in variables;
        All variables used must be created and initiated at the beginning;
        Must follow a naming convention; Output must be a sentence with correct result.
    Variables:
    sphereRadius: Defines sphere's radius
    sphereRadiusCubed: Defines sphere radius cubed
    spherePi: Defines pi
    sphereFraction: Defines the fraction in the equation
    sphereVolume: Defines equation for finding volume given radius
    sphereVolumeRound: Rounds the volume to the 1,000th place

    bookPrice: Defines price of book
    bookWholesaleDiscount: Defines wholesale discount as a decimal
    bookWholesalePrice: Defines price of books with wholesale price
    bookNumber: Defines number of books the store is buying
    bookShipHigh: Defines cost of shipping for books
    bookNoShipHigh: Defines number of books charged high shipping
    bookShipLow: Defines cost of shipping after first book
    bookShipPrice: Defines total cost of shipping given number of books
    bookWholesalePrice: Defines cost of just number of books wholesale
    bookTotalPrice: Defines total price for the book store for the books
    bookTotalPrice: Rounds the price to a penny
    message: Defines the message for the output for the activities
"""
#Imports math so we can use pi
import math;

#Variables for first activity
sphereRadius= 5;
sphereRadiusCubed = sphereRadius**3;
spherePi= math.pi;
sphereFraction= 4/3;
sphereVolume= sphereFraction*spherePi*sphereRadiusCubed;
sphereVolumeRound = round(sphereVolume, 4);
message=f"The volume of a sphere with {sphereRadius} is approximately {sphereVolumeRound} Units Cubed!";
#Prints results
print(message);

#Variables for second activity
bookPrice= 24.95;
bookWholesaleDiscount= 0.4;
bookNumber= 60;
bookShipHigh= 3;
bookShipLow= 0.75;
bookNoShipHigh= 1;
bookWholesalePrice= bookNumber*(bookPrice-(bookPrice*bookWholesaleDiscount));
bookShipPrice= bookShipHigh*bookNoShipHigh+((bookNumber-bookNoShipHigh)*bookShipLow);
bookTotalPrice= bookWholesalePrice+bookShipPrice;
bookTotalPriceRound= round(bookTotalPrice, 3);
message=f"The total price of {bookNumber} books wholesale, for the book store is {bookTotalPriceRound} Dollars!";
#Prints results
print(message);
