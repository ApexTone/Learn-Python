class Sportman:
    def __init__(self, name, medal):
        self.name = name
        self.medal = medal

    def __str__(self):
        return "{:10} {}".format(self.name, self.medal)

    def __lt__(self, other):  # less than method
        d = {"gold": 3, "silver": 2, "bronze": 1}
        if d[self.medal] == d[other.medal]:
            return self.name < other.name
        else:
            return d[self.medal] < d[other.medal]


if __name__ == '__main__':
    data = [
        Sportman("Peter", "silver"),
        Sportman("Taylor", "gold"),
        Sportman("John", "silver"),
        Sportman("Jason", "bronze"),
        Sportman("Tony", "gold"),
        Sportman("Bruce", "gold")
    ]

    s = sorted(data)  # Object can't be sort normally without method overriding
    [print(e) for e in s]
