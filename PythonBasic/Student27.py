class Student:
    # Initialize function: Constructor and attribute
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def get_data(self):
        return self.name+" "+self.major+" "+str(self.gpa)+" "+str(self.is_on_probation)

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
