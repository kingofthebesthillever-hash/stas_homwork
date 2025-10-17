def do_twice(a):
    a()
    a()


def print_row():
    print('+', '-', '-', '-', '-', end=' ')


def print_rows():
    do_twice(print_row)
    print('+')


def print_block():
    print('|        ', end=' ')


def print_blocks():
    do_twice(print_block)
    print('|')


def print_grid():
    print_rows()
    print_blocks()
    print_blocks()
    print_rows()
    print_blocks()
    print_blocks()
    print_rows()


print_grid()
