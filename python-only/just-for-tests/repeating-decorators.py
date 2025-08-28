'''template

def decorator(func):
    def wrapper(*args, **kwargs):
        <some-code>
        func()
        <some-code>
    return wrapper

'''

def decorator(function):
    def wrapper():
        print("Hello", end='')
        function()
        print("world!")
    return wrapper

def f1():
    print(', ', end='')

@decorator
def f2():
    print('_', end='')

f1 = decorator(f1)
f1()

f2()

