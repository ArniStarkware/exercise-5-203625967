import ast


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def greet(name=None):
    if name is None:
        name = 'stranger'
    print(f'Hello, {name}!')


def write_value(path, value):
    with open(path, 'w') as writer:
        writer.write(repr(value))


def read_value(path):
    with open(path) as reader:
        return ast.literal_eval(reader.read())
