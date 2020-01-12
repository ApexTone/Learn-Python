class Glasses:
    def __init__(self, eye, bridge, temple):
        self.eye = eye
        self.bridge = bridge
        self.temple = temple

    @classmethod  # Use to create instance
    def of(cls, frame_str, sep="-"):  # Note that it start with cls not self
        s = frame_str.split(sep)
        return cls(int(s[0]), int(s[1]), int(s[2]))

    @classmethod  # use to make multiple constructor parameter
    def of2(cls, frame_with_weight):
        pass

    def __str__(self):
        return "{} {} {}".format(self.eye, self.bridge, self.temple)


if __name__ == '__main__':
    g1 = Glasses(55, 16, 140)
    g2 = Glasses.of("55-16-140")
    print(g1)
    print(g2)
    print(Glasses.of("55-16-140"))
