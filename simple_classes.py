colors = list()
cities = []  # same as list()

colors.append("blue")
colors.insert(0, "pink")

x = 5   #  x = int(5)
print(type(colors), type(x))

class Dog:
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
d2.bark()