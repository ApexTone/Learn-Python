class Name:
    def __init__(self, title="MR", fname="Noname", lname="Nolastname"):
        self.title = title
        self.fname = fname.strip().title()
        self.lname = lname.strip().title()

    def __str__(self):
        return "{} {} {}".format(self.title, self.fname, self.lname)



class Person:
    def __init__(self, nameEn, nameTh):
        self.nameEn = nameEn
        self.nameTh = nameTh

    def __str__(self):
        return "{}\n{}".format(self.nameEn, self.nameTh)


if __name__ == '__main__':
    p = Person(Name("Mr", "John", "Ja"), Name("นาย", "จอห์น", "จา"))
    print(p)