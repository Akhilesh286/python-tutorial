class Mamel:
    def whak(self):
        print ("whak")


class Dog(Mamel):
    def brak (self):
        print ("brak")


class Cat(Dog):
    pass


dog=Cat()
dog.whak()
dog.brak()

