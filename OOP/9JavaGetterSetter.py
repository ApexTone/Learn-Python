class Student:
    def __init__(self, fname="A", lname="A", blood="X"):
        self.fname = fname
        self.lname = lname
        self.setBlood(blood)

    def __str__(self):
        return "{} {} Blood: {}".format(self.fname, self.lname, self.__blood)

    # Getter Setter
    def setBlood(self, blood):
        if blood.upper() in ["A", "B", "O", "AB"]:
            self.__blood = blood.upper()  # using dunder to make it hard to access
        else:
            raise ValueError["Invalid blood group"]

    def getBlood(self):
        return self.__blood


if __name__ == '__main__':
    s = Student("Tanapol", "Wong-asa", "AB")
    print(s)