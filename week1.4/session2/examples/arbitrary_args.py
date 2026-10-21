# code example on slide 20
def func(*args):
    for arg in args:
        print(arg)


func(1, 2, 3)


# code example on slide 22
def func2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


func2(name="Alice", age=22, programme="BSC")


# code example on slide 23
def greet_people(greeting, *names):
    print(f"{greeting} everyone!")
    for name in names:
        print(f"{greeting}, {name}!")


greet_people("Hello", "Alice", "Bob", "Charlie")
greet_people("Hi")
