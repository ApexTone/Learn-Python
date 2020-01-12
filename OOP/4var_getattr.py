class Person:

    def __init__(self, fname="NoName", lname="NoLastName", age=0):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.age = age

    def __str__(self):
        a = vars(self)  # Return dictionary: key=attr name, value = attr value
        print(a)
        # vars(self) format look likes this
        # svars = ["{} {}".format(k, v) for k, v in a.items()]
        attrs = ("fname", "lname", "age")
        sattrs = ["{:10}: {}".format(a,getattr(self, a)) for a in attrs]  # getattr() return attribute value
        return "\n".join(sattrs)


if __name__ == '__main__':
    p = Person("A", "B", 60)
    print(p)
