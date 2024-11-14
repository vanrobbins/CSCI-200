"""
File Name: lab8OOPBanking
Purpose:

First Created: 11/13/2024
Last Updated: 11/13/2024
Author: Van Robbins
Version 0.5
"""
import os;
import lab8OOPBankingUtility;
from lab8Classes.lab8ClassAcct import AccountHolder;
from lab8Classes.lab8ClassChkAct import Checking;
from lab8Classes.lab8ClassSavAct import Saving;
cwd = os.getcwd();
try:
    bankAccts= open(cwd+"/lab8BankingInfoData/lab8BankActs.csv", 'r');
except:
    #If cannot quit
    print("The system is experiencing technical difficulties");
    quit();

accounts=[];
checkingAccts=[];
savingAccts=[];

j=0;
for i in bankAccts:
    profile=i.split(',');
    lastValue=profile[len(profile)-1];
    profile[len(profile)-1] = lastValue[0:len(lastValue)-1];
    if j>0:
        accounts.append(AccountHolder(profile));
    else:
        j+=1;
        continue;
bankAccts.close;


print("Welcome to Van's Banking Management System");
def mainMenu():
    menuOption=input("1| Create Account\n2| Look up Account\n");
    checkMenuOption=lab8OOPBankingUtility.check(menuOption, 1,3);
    if checkMenuOption==True:
        menuOption=int(menuOption);
        if menuOption==1:#Create Account
            createAccount();
        elif menuOption==2:#Look up Account
            lookUpAccount();
        else:#Complete Transaction
            print("Complete Transaction");
    else:
        mainMenu();

def createAccount():
    print("What type of account would you like to create");
    createAcct= input("1| Checkings\n2| Savings\n3| Both\n");
    checkCreateAcct=lab8OOPBankingUtility.check(createAcct, 1,3);
    if checkCreateAcct==True:
        createAcct=int(createAcct);
        profile=lab8OOPBankingUtility.nameDOB(18,200,35);
        pin=createPin();
        if createAcct==1:
            checkingAcctNum=createChecking(pin);
            profile.append(checkingAcctNum);
            profile.append(None);
            accounts.append(AccountHolder(profile));
            lab8OOPBankingUtility.addDataFile(profile,cwd,"/lab8BankingInfoData/lab8BankActs.csv");
        elif createAcct==2:
            savingAcctNum=createSaving(pin);
            profile.append(None);
            profile.append(savingAcctNum);
            accounts.append(AccountHolder(profile));
            lab8OOPBankingUtility.addDataFile(profile,cwd,"/lab8BankingInfoData/lab8BankActs.csv");
        else:
            checkingAcctNum=createChecking(pin);
            savingAcctNum=createSaving(pin);
            profile.append(checkingAcctNum);
            profile.append(savingAcctNum);
            accounts.append(AccountHolder(profile));
            lab8OOPBankingUtility.addDataFile(profile,cwd,"/lab8BankingInfoData/lab8BankActs.csv");
    mainMenu();

def createPin():
    pin=input("Create a 4 digit pin for your new account: ");
    checkpin=lab8OOPBankingUtility.check(pin,0000,9999);
    if checkpin==True:
        if len(pin)==4:
            return(pin);
        else:
            print("Please Try Again! Ensure Pin is 4 Digits!")
            createPin();
    else:
        createPin();

def createChecking(pin):
    initChecking();
    lastAccountNumber=checkingAccts[len(checkingAccts)-1].getAccountNumber();
    newAccountNumber=int(lastAccountNumber)+1;
    newAccount=[newAccountNumber,pin,0];
    checkingAccts.append(Checking(newAccount));
    lab8OOPBankingUtility.addDataFile(newAccount,cwd,"/lab8BankingInfoData/lab8ChkActs.csv");
    return newAccountNumber;


def createSaving(pin):
    initSaving();
    lastAccountNum=savingAccts[len(savingAccts)-1].getAccountNumber();
    newAccountNumber=int(lastAccountNum)+1;
    newAccount=[newAccountNumber,pin,0];
    savingAccts.append(Saving(newAccount));
    lab8OOPBankingUtility.addDataFile(newAccount,cwd,"/lab8BankingInfoData/lab8SavActs.csv");
    return newAccountNumber;

def initChecking():
    try:
        checkings= open(cwd+"/lab8BankingInfoData/lab8ChkActs.csv", 'r');
    except:
    #If cannot quit
        print("The system is experiencing technical difficulties");
        quit();
    j=0;
    for i in checkings:
        profile=i.split(',');
        lastValue=profile[len(profile)-1];
        profile[len(profile)-1] = lastValue[0:len(lastValue)-1];
        if j>0:
            checkingAccts.append(Checking(profile));
        else:
            j+=1;
            continue;

def initSaving():
    try:
        savings= open(cwd+"/lab8BankingInfoData/lab8SavActs.csv", 'r');
    except:
        #If cannot quit
        print("The system is experiencing technical difficulties");
        quit();
    j=0;
    for i in savings:
        profile=i.split(',');
        lastValue=profile[len(profile)-1];
        profile[len(profile)-1] = lastValue[0:len(lastValue)-1];
        if j>0:
            savingAccts.append(Saving(profile));
        else:
            j+=1;
            continue;

def lookUpAccount():
    i=0;
    print("How would you like to lookup the account?");
    lookAcct= input("1| Account Holder Name and DOB\n2| Account Number\n");
    checklookAcct=lab8OOPBankingUtility.check(lookAcct, 1,2);
    if checklookAcct==True:
        lookAcct=int(lookAcct);
        if lookAcct==1:
            lookUpName=lab8OOPBankingUtility.nameDOB(18,200,35);
            while i < len(accounts):
                if accounts[i].getName()==f"{lookUpName[0]} {lookUpName[1]}" and accounts[i].getDOB()==f"{lookUpName[2]}":
                    print(f"\nAccount(s) Found {accounts[i]}")
                    break;
                i+=1;
            userChecking=accounts[i].getChecking();
            userSaving=accounts[i].getSaving();
            transact=input("Would you like to make a transaction on one of these accounts?\n1|Yes\n2|No\n")
            while checkTransact==False:
                transact=input("Would you like to make a transaction on one of these accounts?\n1|Yes\n2|No\n");
                checkTransact=lab8OOPBankingUtility.check(transact,1,2);
            transact=int(transact);
            if transact==1:
                if userChecking==None:
                    transaction(userSaving);
                elif userSaving==None:
                    transaction(userChecking);
                else:
                    chkOrSave=input("Checkings or Savings?\n1| Checkings\n2| Savings");
                    checkChkOrSave=lab8OOPBankingUtility.check(chkOrSave,1,2);
                    while checkChkOrSave==False:
                        chkOrSave=input("Checkings or Savings?\n1| Checkings\n2| Savings");
                        checkChkOrSave=lab8OOPBankingUtility.check(chkOrSave,1,2);
                    chkOrSave=int(chkOrSave)
                    if chkOrSave==1:
                        transaction(userChecking);
                    else:
                        transaction(userSaving);
            else:
                mainMenu();   
        else: 
            lookUpAccountNum=input("Enter Account Number: ");
            while i < len(accounts):
                if accounts[i].getChecking()==lookUpAccountNum or accounts[i].getSaving()==lookUpAccountNum:
                    print(f"\nAccount(s) Found\n{accounts[i]}")
                    break;
                i+=1;
            transact=input("Would you like to make a transaction on this account?\n1|Yes\n2|No\n")
            checkTransact=lab8OOPBankingUtility.check(transact,1,2);
            while checkTransact==False:
                transact=input("Would you like to make a transaction on this account?\n1|Yes\n2|No\n");
                checkTransact=lab8OOPBankingUtility.check(transact,1,2);
            transact=int(transact);
            if transact==1:
                transaction(lookUpAccountNum)
            else:
                mainMenu();
                

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
    checkDepotOWith=lab8OOPBankingUtility.check(depotOWith,1,2);
    while checkDepotOWith==False:
        depotOWith=input("Would You Like to\n1| Deposit\n2| Withdraw\n");
        checkDepotOWith=lab8OOPBankingUtility.check(depotOWith,1,2);
    depotOWith=int(depotOWith);
    if depotOWith==1:
        depositValue=input("Max Deposit 10,000\n");
        checkDeposit=lab8OOPBankingUtility.check(depositValue,1,10000);
        while checkDeposit==False:
            depositValue=input("Max Deposit 10,000\n");
            checkDeposit=lab8OOPBankingUtility.check(depositValue,1,10000);
        account.deposit(depositValue);
        print(account);
    else:
        withdrawValue=input("Max Withdraw 10,000\n");
        checkWithdraw=lab8OOPBankingUtility.check(withdrawValue,1,10000);
        while checkWithdraw==False:
            withdrawValue=input("Max Withdraw 10,000\n");
            checkWithdraw=lab8OOPBankingUtility.check(withdrawValue,1,10000);
        account.withdraw(withdrawValue)
        print(account);
mainMenu();