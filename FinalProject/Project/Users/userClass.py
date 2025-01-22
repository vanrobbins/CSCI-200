class User:
    def __init__(self, fn, ln, un):
        """
        Initialize the User with first name, last name, and username.
        """
        self.first = fn
        self.last = ln
        self.username = un
            
    def __str__(self):
        """
        Return a string representation of the User in 'First Last - username' format.
        """
        return f"{self.first} {self.last} - {self.username}"

    def getFirstNm(self):
        """
        Return the user's first name.
        """
        return self.first

    def getLastNm(self):
        """
        Return the user's last name.
        """
        return self.last

    def getName(self):
        """
        Return the full name of the user.
        """
        return f"{self.first} {self.last}"

    def getUsername(self):
        """
        Return the username of the user.
        """
        return self.username

    def setFirstNm(self, newFirst):
        """
        Set the user's first name.
        """
        self.first = newFirst

    def setLastNm(self, newLast):
        """
        Set the user's last name.
        """
        self.last = newLast

    def setUsername(self, newUsername):
        """
        Set the user's username.
        """
        self.username = newUsername
