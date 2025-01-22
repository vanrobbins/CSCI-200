from lab9Classes.lab9ClassAccount import Account;
class Checking(Account):
    pin=None;
    def __str__(s):
        return f"Checking Account: {s.accountNumber} Balance: ${s.balance:.2f}";
    def setPin(s,p):
        if s.pin==None:
            s.pin=p;
        else:
            oldPin=input("Input current Pin");
            if oldPin==s.pin:
                newPin=input("Input new Pin");
                s.pin= newPin;