

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.price = price
        self.shares = shares

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        if self.shares < shares:
            self.shares = 0
        else:
            self.shares -= shares