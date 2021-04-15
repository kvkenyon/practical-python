from typedproperty import String, Int, Float

class Stock:
    __slots__ = ('_name', '_price', '_shares')

    name = String('name')
    shares = Int('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.price = price
        self.shares = shares
    
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        if self.shares < shares:
            self.shares = 0
        else:
            self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"