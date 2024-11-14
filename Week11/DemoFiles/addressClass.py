"""
File name: addressClass.py
Purpose: This file defines the Address class
Author: Lingma Lu
Create date: 10/25/2023
Last update date:10/25/2023
version: 1.1
"""

class Address:
    streetNumber = "";
    optional = "";
    streetName = "";
    city = "";
    state = "";
    zip = "";

    def __init__(self, sn="", op="", sa="", ct="", st="",zp="", cn="" ): #can define default values in case no arguments are provided
        self.streetNumber = sn;
        self.optional = op;
        self.streetName = sa;
        self.city = ct;
        self.state = st;
        self.zip = zp;
        self.country = cn;

    def __str__(self):
        return self.streetNumber + ", " + self.optional + ", " + self.streetName + ", " + self.city + ", " + self.state + ", " + self.zip + ", " + self.country;
