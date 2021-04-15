# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self.__holdings = holdings

    def __iter__(self):
        return self.__holdings.__iter__()

    def __len__(self):
        return len(self.__holdings)

    def __getitem__(self, index):
        return self.__holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self.__holdings)
    
    @property
    def total_cost(self):
        return sum(h.cost for h in self.__holdings) 

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()

        for s in self.__holdings:
            total_shares[s.name] += s.shares

        return total_shares
    