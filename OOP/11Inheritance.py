import re

class Person:
    def __init__(self, fname="Noname", lname="Nolastname"):
        self.fname = fname.strip().title()
        self.lname = lname.strip().title()

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)


class Student(Person):  # Inherited from Person class
    def __init__(self, id="000000", fname="noname", lname="nolastname"):
        super().__init__(fname, lname)
        self.id = self.remove_non_digit(id)

    @staticmethod
    def remove_non_digit(s):
        return re.sub(r"[\D]", "", s)

    def email(self):
        return "{}.kmitl.ac.th".format(self.id)

    def __str__(self):
        return "{} {}".format(self.id, super().__str__())  # return id + superclass format


class ExchangeStudent(Student):
    def __init__(self, partner_univ="KMITL", id="000000", fname="noname", lname="nolastname"):
        super().__init__(id, fname, lname)  # Use superclass constructor
        self.partner_univ = partner_univ

    def foo(self,s):
        return self.remove_non_digit(s)

    def __str__(self):
        return "{} {}".format(super().__str__(), self.partner_univ)


if __name__ == '__main__':
    s1 = Student(id="asdf525--000", fname="A", lname="B")
    print(s1)
    print(s1.email())

    e1 = ExchangeStudent();
    print(e1)


