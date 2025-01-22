from lab9Classes.lab9ClassAccount import Account;
class Saving(Account):
    def __str__(s):
        return f"Saving Account: {s.accountNumber} Balance: ${s.balance:.2f}";
    def applyInterest(s):
        s.balance*=1.04;
    
