class Camera:
    def shoot(self):
        print("Shoot photo")

    def browse(self):
        print("Browse photo")


class Phone:
    def call(self,num):
        print("Calling {}".format(num))


class MediaPlayer:
    def browse(self):
        print("Browsing media")


class SmartPhone(Phone, Camera, MediaPlayer):
    def share(self):
        print("Sharing...")


if __name__ == '__main__':
    s = SmartPhone()

    # If multiple function have same name, it will choose the first superclass function
    s.browse()