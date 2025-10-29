class Hello:
    def __init__(self, whom):
        self.whom = whom

    def __call__(self):
        print(f"Hello, {self.whom}")

h = Hello("world")
hh = Hello("Mom")
h()  # shortcut for h.__call__()
hh()
h()
h()