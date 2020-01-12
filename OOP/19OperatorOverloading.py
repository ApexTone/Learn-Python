class FootInch:
    def __init__(self, foot, inch):
        self.foot = foot
        self.inch = inch
        self.inches = self.foot * 12 +self.inch

    def __str__(self):
        return "{}' {}''".format(self.foot, self.inch)

    def __add__(self, other):  # Overload +
        x = self.inches + other.inches
        f = x // 12  # int division
        i = x % 12
        return FootInch(f, i)

    def __sub__(self, other):  # Overload -
        x = self.inches - other.inches
        f = x // 12  # floor division
        i = x % 12
        return FootInch(f, i)


if __name__ == '__main__':
    m1 = FootInch(5, 7)
    m2 = FootInch(3, 9)
    print(m1 + m2)  # Can't be call without overloading the operator
    print(m1.__add__(m2))
    print(m1 - m2)
    print(m1.__sub__(m2))
