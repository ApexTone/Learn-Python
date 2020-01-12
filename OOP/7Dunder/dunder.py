# dunder is __


class Alpha:
    normal = 1
    _lucky = 13
    __secret = 777  # name mangled: Change name to _CLASSNAME__ATTRNAME

    def fx(self):
        print("fx")

    def _fy(self):
        print("fy")

    def __fz(self):  # name mangled, final method: Can't be override
        print("fz")


class Beta(Alpha):  # Inherited from Alpha
    def __fz(self):  # This is a new method, not overriding old method
        print("fz in Beta")


class __Gamma():  # Can be use normally but can't be use by "from MODULE import *"
    def bar(self):
        print("Hello in Gamma")


if __name__ == '__main__':  # Front and back dunder, for Python internal use only.
    print(Alpha.normal)
    print(Alpha._lucky)

    print(Alpha.__dict__)  # Show attr: Show that __secret should be called using _Alpha__secret
    # print(Alpha.__secret)  # Can't access this
    print(Alpha._Alpha__secret)  # Access dunder member

    Alpha.normal = 99
    Alpha._lucky = 123
    Alpha.__secret = 999
    print(Alpha.normal)
    print(Alpha._lucky)
    print(Alpha.__secret)  # This is not __secret in the class! It's a new attr
    print(Alpha._Alpha__secret)  # Real __secret from class

    a = Alpha()
    a.fx()
    a._fy()
    a._Alpha__fz()

    b = Beta()
    b._Beta__fz()
    b._Alpha__fz()

    c = __Gamma()
    c.bar()