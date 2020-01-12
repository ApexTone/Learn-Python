# _ use for coding style and encapsulation

# You can also allow import * to import all things you WANT too
# __all__ = ["circle", "Alpha", "_rectangle", "not_a_secret", "_secret", "_Beta"]


# Use as generic looping item without usage
for _ in range(5):
    print("Hello")

# Can still be use as variable
for _ in range(5):
    print(_)

# Use as private member sign for universal understanding
# Member with _ in front won't be import in "from MODULE import *" unless specifically told to do so
_secret = "secret member"
not_a_secret = "not secret member"


def _rectangle(w, h):
    return w*h


def circle(r):
    return 22/7*r*r


class Alpha:
    @staticmethod
    def foo():
        print("Alpha")


class _Beta:
    @staticmethod
    def foo():
        print("_Beta")

