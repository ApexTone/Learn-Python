class Person:
    # Constructor
    # Python can't overload method, so it can only contain only 1 implementation
    # Use this implementation to make default constructor
    def __init__(self, first_name="NoName", last_name="NoLastName", country="Thailand"):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.country = country.capitalize()

    # Something like toString() overriding
    def __str__(self):
        return "{} {} {}".format(self.first_name,self.last_name,self.country)


if __name__ == '__main__':
    # declaring object
    p1 = Person()
    print(p1)

    p2 = Person(last_name="ThisLastName")
    print(p2)

    p3 = Person("FirstName", "LastName")
    print(p3)

    p4 = Person("John", "Conner", "USA")
    print(p4)




