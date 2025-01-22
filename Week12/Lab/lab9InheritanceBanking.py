"""
File Name: lab9OOPBanking
Purpose:

First Created: 11/13/2024
Last Updated: 11/13/2024
Author: Van Robbins
Version 0.5
"""
import os;
import lab9InheritanceBankingUtility;
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
                            account.setPin(accountPin);
                        else:
                            print(f"Pin not found for account{accountInfo[0]}")

                    elif accountInfo[1]=="SAV":
                        account = Saving(accountInfo[0], accountInfo[1], float(accountInfo[2]));#Create a Saving Checking object
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
#MAIN MENU CONTROLS FLOW OF PROGRAM
def mainMenu():
    menuOption=input("1| Create Account\n2| Look up Account/Make Transaction\n3| Exit\n");
    checkMenuOption=lab9InheritanceBankingUtility.check(menuOption, 1,3);
    #Check if menu option is a valid input
    if checkMenuOption==True:
        menuOption=int(menuOption);
        if menuOption==1:#Create Account
            newExisting();
        elif menuOption==2:#Look up Account
            profile=findProfile();
        else:#Exit Program
            quit();
    #If menu option entered is not valid but program continues send back to mainmenu to try again
    else:
        mainMenu();

#NEW OR RETURNING USER
def newExisting():
    #ASK USER IF ALREADY HAVE ACCOUNT
    newOrExisting=input("Are you a new customer or existing customer?\n1| New\n2| Existing\n");
    checkNewOrExisting=lab9InheritanceBankingUtility.check(newOrExisting,1,2);
    if checkNewOrExisting==True:
        newOrExisting=int(newOrExisting);
        if newOrExisting==1:
            createProfile();
        else:
            #EXISTING USER ADD ACCOUNT
            profile=findProfile();
            createAccount(profile,False);
            
    else:
        newExisting();

#CREATE NEW PROFILE
def createProfile():
    print("Let's get your info");
    newProfile=lab9InheritanceBankingUtility.nameDOB(18,200,2,35);
    print(newProfile);
    profileObject=AccountHolder(newProfile[0],newProfile[1],newProfile[2],[None,None,None,None]);
    createAccount(profileObject,True);

#CREATE ACCOUNT
def createAccount(profile,newAccount):
    #SETTING PIN FOR NEW ACCOUNT
    if newAccount==True:
        newAccountPin=createPin();
    #ASKS EXISTING USER IF WANT TO USE OLD PIN OR MAKE NEW PIN FOR NEW ACCOUNT
    else:
        #CHECKINGS OR SAVINGS; SAVINGS ACCOUNT PIN TIED TO CHECKING ACCOUNT SO DON'T ASK IF CREATING SAVINGS AND ONLY HAVE ONE CHECKING
        existingOrNewPin=input("Would you like to create a new pin or use old pin?\n1| New Pin \n 2| Old Pin\n");
        checkExistingOrNewPin=lab9InheritanceBankingUtility.check(existingOrNewPin);
        if checkExistingOrNewPin==True:
            existingOrNewPin=int(existingOrNewPin);
            if existingOrNewPin==1:
                newAccountPin=createPin();
            else:
                #Print only profiles accounts that are checking accounts;
                print(f"Which account ")
    
    #FIND LARGEST ACCOUNT NUMBER FUNCTION
    largestAccountNum=1#PlaceHolder
    newAccountNumber=largestAccountNum+1;
    
    profile.Checking.setAccount(newAccountNumber);
    profile.Saving.setAccount(newAccountNumber);
    
#FIND EXISTING PROFILE
def findProfile():
    i=0;
    print("How would you like to lookup the account?");
    lookUpMethod= input("1| Account Holder Name and DOB\n2| Account Number\n");
    checkLookUpMethod=lab9InheritanceBankingUtility.check(lookUpMethod, 1,2);
    #CHECK IF INPUT VALID
    if checkLookUpMethod==True:
        #ASKS USER HOW THEY WOULD LIKE TO FIND THE PROFILE
        lookUpMethod=int(lookUpMethod);
        #FIND VIA NAME AND DOB
        if lookUpMethod==1:
            lookUpName=lab9InheritanceBankingUtility.nameDOB(18,200,3,35);
            while i < len(accounts):
                if (accounts[i].getName()==f"{lookUpName[0]} {lookUpName[1]}") and (accounts[i].getDOB()==f"{lookUpName[2]}"):
                    print("Profile Found")
                    #RETURN PROFILE
                    return accounts[i];
                i+=1;
        #FIND VIA ACCOUNT NUMBER
        else:
            global searchAccount;
            lookUpAccountNum=input("Enter Account Number: ");
            while i < len(accounts):#Search array of profiles
                for singleAccount in accounts[i].account:#Get single account in profiles account array
                    if singleAccount.getAccount()==lookUpAccountNum:#Compare account number to account number seeking
                        print("Profile Found");
                        #Return Profile
                        searchAccount=lookUpAccountNum;
                        return accounts[i];#Return account object
                i+=1;
        #ACCOUNT NOT FOUND IN SEARCH ASK USER IF WANT TO TRY AGAIN
        print("Account Not Found")
        tryAgain=lab9InheritanceBankingUtility.again()
        if tryAgain==True:
            findProfile();
    #INPUT INVALID USER OPTED TO TRY AGAIN
    else:
        findProfile();

#CREATE NEW PIN
def createPin():
    pin=input("Create a 4 digit pin for your new account: ");
    checkpin=lab9InheritanceBankingUtility.check(pin,0,9999);
    if checkpin==True:
        if len(pin)==4:
            return(pin);
        else:
            print("Please Try Again! Ensure Pin is 4 Digits!")
            createPin();
    else:
        createPin();

'''

def transaction(account):
    i=0;
    if int(account)<200000:
        initChecking();
        while i < len(checkingAccts):
            if checkingAccts[i].getAccountNumber()==int(account):
                break;
            else:
                i+=1;
        pin=input("Enter Pin");
        print(i);
        
        if pin==checkingAccts[i].getPin():
            print(checkingAccts[i]);
            account=checkingAccts[i];
        else:
            print("Wrong Pin");
            mainMenu();
        
    else:
        initSaving();
        while i < len(savingAccts):
            if savingAccts[i].getAccountNumber()==int(account):
                break;
            else:
                i+=1;
        pin=input("Enter Pin");
        if pin==savingAccts[i].getPin():
            print(savingAccts[i]);
            account=savingAccts[i];
        else:
            print("Wrong Pin");
            mainMenu();
    depotOWith=input("Would You Like to\n1| Deposit\n2| Withdraw\n");
    checkDepotOWith=lab9InheritanceBankingUtility.check(depotOWith,1,2);
    while checkDepotOWith==False:
        depotOWith=input("Would You Like to\n1| Deposit\n2| Withdraw\n");
        checkDepotOWith=lab9InheritanceBankingUtility.check(depotOWith,1,2);
    depotOWith=int(depotOWith);
    if depotOWith==1:
        depositValue=input("Max Deposit 10,000\n");
        checkDeposit=lab9InheritanceBankingUtility.check(depositValue,1,10000);
        while checkDeposit==False:
            depositValue=input("Max Deposit 10,000\n");
            checkDeposit=lab9InheritanceBankingUtility.check(depositValue,1,10000);
        account.deposit(depositValue);
        print(account);
    else:
        withdrawValue=input("Max Withdraw 10,000\n");
        checkWithdraw=lab9InheritanceBankingUtility.check(withdrawValue,1,10000);
        while checkWithdraw==False:
            withdrawValue=input("Max Withdraw 10,000\n");
            checkWithdraw=lab9InheritanceBankingUtility.check(withdrawValue,1,10000);
        account.withdraw(withdrawValue)
        print(account);
mainMenu();
'''

initDataObjects();
print("Welcome to Van's Banking Management System")
mainMenu();
