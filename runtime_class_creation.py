
class Animal:
    def breathe(self):
        print("breathing...")

class Cat(Animal):
    pass

c = Cat()
c.breathe()

Dog = type('Dog', (Animal,), {'bark': lambda self: print("WOOF")})

d = Dog()
d.breathe()
d.bark()