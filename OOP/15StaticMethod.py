class Person:
    def __init__(self, fname="NoF", lname="NoL", w_kg=0.0, h_cm=0.0):
        self.fname = fname
        self.lname = lname
        self.w_kg = w_kg
        self.h_cm = h_cm

    def bmi(self):  # Normal method
        return self.w_kg/(self.h_cm/100)**2  # pow(h_cm,2)

    @staticmethod  # Static method won't alter self data
    def kg_pound(kg):  # Static method can't access attr since it can be called without instance
        return kg * 2.020462

    @staticmethod
    def cm_inch(cm):
        return cm * 0.393701

    def __repr__(self):
        return repr((self.fname, self.lname, self.w_kg, self.kg_pound(self.w_kg), self.h_cm, self.cm_inch(self.h_cm)))


if __name__ == '__main__':
    p = Person(w_kg=50, h_cm=160)
    print(p.bmi())  # Normal method
    print(Person.cm_inch(123))  # Static method
