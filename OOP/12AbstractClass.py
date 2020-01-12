from abc import ABC, abstractmethod  # Abstract Base Class


class Member(ABC):  # Abstract class can't be use to create instance
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "{} {} {}".format(self.fname, self.lname, self.id)

    @abstractmethod  # Use to block creation of instance
    def discount(self, amount):  # Feels like interface in JAVA
        pass

    def full_name(self):
        return "{} {}".format(self.fname, self.lname)


class GoldMember(Member):
    def discount(self, amount):
        return amount*0.1


class SilverMember(Member):
    def discount(self, amount):
        return amount*0.05


if __name__ == '__main__':
    # m = Member("007", "James", "Bond")  # Abstract class can't have instance
    g = GoldMember("007", "James", "Bond")
    print(g)
    print(g.full_name())