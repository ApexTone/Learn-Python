class Wallet:
    def __init__(self, a=0):
        self.amount = a

    def earn(self, a):
        self.amount += a

    def spend(self, a):
        self.amount -= a

    def __str__(self):
        a = vars(self)
        print(a)
        return ""


if __name__ == '__main__':
    dad = Wallet()
    dad.earn(100)
    print("Dad's wallet: ", dad)

    # Referencing to the same object
    mom = dad
    print(mom is dad)  # Return boolean as true
    print("Mom's wallet: ", mom)
    mom.spend(20)

    print("Dad's wallet:", dad)
    print("Mom's wallet:", mom)

    print(id(dad), id(mom))  # Same memory

    kid = Wallet(200)
    mom = kid   # Change mom reference
    print(mom is kid)
    print(id(dad), id(mom), id(kid))


