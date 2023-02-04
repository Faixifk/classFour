#Python wallet code

#code

class Wallet:

    def __init__(self, balance):

        self.balance = balance

    def setAccount(self, balance):

        self.balance = balance

    def getAccount(self):

        return self.balance

    def removeAccount(self):

        self.balance = 0
