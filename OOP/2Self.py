class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):
        return self.gold+self.silver+self.bronze
# NOTE: We can use other word than self too! Ex: this, me, etc.

    def dummy(this, a, b): # as can be seen here
        return a+b


if __name__ == '__main__':
    th = Medal("Thailand", 5, 3, 2)

    # How we usually call
    print(th.total())  # self is like passing object itself into the method
    # How it's actually call
    print(Medal.total(th))

    print(th.dummy(2, 3))

    # Declaring new attribute
    th.rank = 20
    print(th.rank)
