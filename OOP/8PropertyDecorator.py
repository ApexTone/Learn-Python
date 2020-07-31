class Student:
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    def full_name(self):  # Getter in java: Prevent editing
        return "{} {}".format(self.fname, self.lname)

    @property  # Use for getting specific data from whole data EX: ID, fullname
    def full_name2(self):
        return "{} {}".format(self.fname, self.lname)

    # KMITL id: 62:joined_year/ 01:faculty/ 0356:running_number
    @property
    def joined_year(self):
        return self.id[:2] # from [0,2)

    @property
    def joined_faculty(self):
        return self.id[2:4]

    @property
    def sequence(self):
        return self.id[4:]

    @property
    def email(self):
        return "{}{}@kmitl.ac.th".format(self.fname, self.id)


if __name__ == '__main__':
    s = Student("62010356", "Tanapol", "Wong-asa")
    print(s.full_name())

    # Calling like a data field
    print(s.full_name2)
    print(s.joined_year)
    print(s.joined_faculty)
    print(s.sequence)
    print(s.email)
