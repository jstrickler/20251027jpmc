
colors = ['red', 'blue', 'green']
print(hasattr(colors, 'append'))
a = getattr(colors, 'append')
a('pink')  # colors.append('pink')
print(colors)

class Dog:
    pass

d = Dog()

setattr(Dog, 'bark', lambda self: print("Woof! Woof!"))
d.bark()