# Keyword arguments
def add(*args):
    return sum(args)


print(add(1, 6, 7, 8, 3))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs.get('add')
    n *= kwargs.get('multiply')
    print(n)


calculate(2, add=3, multiply=5)
