"""
File Name: lab9InheritanceBanking
Purpose:
Interpret CSV file and create objects based on file. 
Creates Account Holder class with multiple Account classes.
Checking and Saving account subclasses of Account are created based on its type.
If Checking account looks for pin of account in pin CSV and sets it to object
If Saving account sets banks current interest rate to object
Does not include changing csv or adding to csv
First Created: 11/13/2024
Last Updated: 11/19/2024
Author: Van Robbins
Version 0.5
"""
import os;
from lab9Classes.lab9ClassAccountHolder import AccountHolder;
from lab9Classes.lab9ClassAccount import Account;
from lab9Classes.lab9ClassChecking import Checking;
from lab9Classes.lab9ClassSaving import Saving;
#Get Current Directory
cwd = os.getcwd();
accounts = [];  #To store processed account holders
searchAccount="";
#INITIALIZES EXISTING ACCOUNT OBJECTS
def initDataObjects():
    global accounts
    #Try to open Data File; Create Stored Profile Array
    try:
        bankAccts= open(cwd+"/lab9Data/lab9BankActs.csv", 'r');
    except:
        #If cannot quit
        print("The system is experiencing technical difficulties");
        quit();
    lines = bankAccts.readlines() #Read all lines in file
    for line in lines[1:]:  #Iterating through bank accounts
        line= line.strip(); #Remove extra spaces or new lines
        profile = line.split(','); #Splitting profile data by commas
        lastValue=profile[-1];
        lastValue = lastValue.split('-');  #Remove the last character, split by '-'
        #Split lastValue into 3 lists by space
        nestedData = [i.split(' ') for i in lastValue];
        #Zip the nested data to align corresponding elements
        if len(nestedData) == 3:  #Ensure the structure is correct
            try:
                transformedData = [list(item) for item in zip(*nestedData)]
                # Create Account objects for each transformed entry
                accountObjects = []  #Initialize an empty list
                for accountInfo in transformedData:#Iterate through the transformed data
                    if accountInfo[1]=="CHK":  
                        account = Checking(accountInfo[0], accountInfo[1], float(accountInfo[2]));#Create an Account Checking object
                        accountPin=lookPin(accountInfo[0]);
                        if accountPin is not None:#Pin Found
                            account.setPin(accountPin);#Set accounts pin to found pin
                        else:
                            print(f"Pin not found for account{accountInfo[0]}")

                    elif accountInfo[1]=="SAV":
                        account = Saving(accountInfo[0], accountInfo[1], float(accountInfo[2]));#Create a Saving Checking object
                        account.setInterest(4);
                    else:
                        account = Account(accountInfo[0], accountInfo[1], float(accountInfo[2]));
                    accountObjects.append(account)
                # Create an AccountHolder object
                accountHolder = AccountHolder(profile[0], profile[1], profile[2], accountObjects)
                accounts.append(accountHolder)              
            except ValueError as e:
                print(f"Error processing account data: {e}")
                continue
        else:
            print("Data is not in the expected format");
            continue  # Skip this profile if the structure is incorrect
#LOOKS FOR PINS TO ASSIGN TO ACCOUNT OBJECTS
def lookPin(accountNum):
    try:
        pinFile=open(cwd+"/lab9Data/lab9Pins.csv",'r');#Open pin file
    except:
        print("Error opening pins");
    lines = pinFile.readlines();
    for i in lines[1:]:  # Skip the first line if it's a header
            i = i.strip()  # Remove any leading/trailing whitespace or newline characters
            pinData = i.split(',');
            accNum , pin = pinData;
            if accNum == accountNum:
                return pin;
initDataObjects();

#TEST ACCOUNT
testAccount=accounts[0];
testAccountChecking=(testAccount.getAccount())[0];
testAccountSaving=(testAccount.getAccount())[1];
print("Current Pin is 9999")
testAccountChecking.setPin(None);#CURRENT PIN IS 9999
testAccountSaving.deposit(100.42);
testAccountSaving.applyInterest();
print(testAccount);
print("New Checking Account Pin");
print(testAccountChecking.getPin());
print("Saving Account Interest");
print(testAccountSaving.getInterest());
