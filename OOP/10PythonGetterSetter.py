class Student:
    def __init__(self, fname="B", lname="B", blood="X"):
        # This all call for setter, they aren't attr
        self.fname = fname
        self.lname = lname
        self.blood = blood

    def __str__(self):
        return "{} {} Blood: {}".format(self.fname, self.lname, self.blood)

    # Note the usage of dunder here to prevent easy random access
    # Getter/Setter: Have same name
    @property
    def blood(self):
        return self.__blood  # The real attr

    @blood.setter
    def blood(self, blood):
        if blood.upper() in ["A", "B", "O", "AB"]:
            self.__blood = blood.upper()
        else:
            raise ValueError["Invalid blood group"]

    @property
    def fname(self):
        return self.__fname  # The real attr

    @fname.setter
    def fname(self, fname):
        self.__fname = fname.strip().title()

    @property
    def lname(self):
        return self.__lname  # The real attr

    @lname.setter
    def lname(self, lname):
        self.__lname = lname.strip().title()


if __name__ == '__main__':
    s = Student("asdf", "ghj", "A")
    print(s)
    s.blood = "B"  # Calling setter
    print(s.blood)  # Calling getter
    print(s.__dict__)

