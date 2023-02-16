def outer(x):
    def inner(y):
        return x + y
    return inner

# add_five = outer(5)
# result = add_five(6)
# print(result)  # prints 11
#
# # Output: 11
print(outer(5)(7))

def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10

#dekorator
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

# decorated_func = make_pretty(ordinary)
# decorated_func()

make_pretty(ordinary)()


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

