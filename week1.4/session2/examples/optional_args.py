# code examples on slide 5
for item in range(5):
    print(item, end=":")

print("hello", "world", "there", sep='@')


# code example on slide 6
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


print(greet("Alice", "Hi", "."))     # Hi, Alice.
print(greet("Bob", "Good morning"))  # Good morning, Bob!
print(greet("Charlie"))              # Hello, Charlie!
