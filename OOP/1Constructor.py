class Person:
    # Constructor
    # Python can't overload method
    # Use this implementation to make default constructor
    def __init__(self, fname="NoName", lname="NoLastName", country="Thailand"):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.country = country.capitalize()

    # Something like toString() overriding
    def __str__(self):
        return "{} {} {}".format(self.fname,self.lname,self.country)


if __name__ == '__main__':
    p1 = Person()
    print(p1)

    p2 = Person(lname="ThisLastName")
    print(p2)

    p3 = Person("FirstName","LastName")
    print(p3)

    p4 = Person("asdf","fff","USA")
    print(p4)




