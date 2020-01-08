class Chef:

    def make_chicken(self):
        print("Make chicken")

    def make_salad(self):
        print("Make salad")

    def make_special_dish(self):
        print("Make stake")


class ChineseChef(Chef):

    def make_fried_rice(self):
        print("Make fried rice")
    def make_special_dish(self):
        print("Make Ching Chong something")


# Need no default constructor
myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

chin = ChineseChef()
chin.make_special_dish()
chin.make_fried_rice()