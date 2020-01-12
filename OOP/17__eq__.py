class Score:
    def __init__(self, point=0):
        self.point = point

    def __str__(self):
        return "{}".format(self.point)

    def __eq__(self, other):
        return self.point == other.point


if __name__ == '__main__':
    s1 = Score(55)
    s2 = Score(55)
    print(s1)
    print(s2)

    # Class comparing will compare it with address id
    print(s1 == s2)  # Got overridden by __eq__()
    # But with __eq__() it will compare value that you code it
    print(s1.__eq__(s2))


