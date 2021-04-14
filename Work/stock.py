class Stock:
    __slots__ = ('name', 'price', '__shares')
    def __init__(self, name, shares, price):
        self.name = name
        self.price = price
        self.__shares = shares
    
    @property
    def shares(self):
        return self.__shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self.__shares = value

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