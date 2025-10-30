
#         type hint
def greet(whom: str) -> None:
    print(f"Hello, {whom}")

greet("world")
greet("universe")
greet("Mom")
greet(123)
greet(['spam', 'ham', 'eggs'])

x: int | float
x = 5
x = 5.9
x = "abc"

