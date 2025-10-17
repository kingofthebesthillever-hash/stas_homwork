def do_twice(f):
    f()
    f()


def print_spam():
    print('спам')


def do_twice(f, value):
    f(value)
    f(value)

def print_spam(message):
    print(message)

do_twice(print_spam, 'спам')
