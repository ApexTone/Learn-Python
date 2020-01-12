class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):
        return self.gold+self.silver+self.bronze

    def __str__(self):  # toString()->Prioritize over __repr__
        return "Country:{:15}\n Gold:{:5} Silver:{:3} Bronze:{:3}\n Total:{:4}".format(self.country, self.gold, self.silver, self.bronze, self.total())

    def __repr__(self):  # string representation, for quick referencing in coding
        return "{} {}".format(self.__class__.__name__, repr((self.country, self.gold, self.silver, self.bronze, self.total())))


if __name__ == '__main__':
    th = Medal("Thailand",5,6,7)
    # __str__
    print(th)
    # random printing
    print(th.country, "G", th.gold, "S", th.silver, "B", th.bronze, "Total", th.total())

    medals = [
        Medal("Greece", 5, 9, 10),
        Medal("China", 5, 2, 1),
        Medal("Vietnam", 5, 6, 1)
    ]
    for country in medals:
        print(country)
