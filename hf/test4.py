def my_func(*args) -> None:
    for a in args:
        print(a, end=' ')
    if args:
        print()


def my_func2(**args) -> None:
    for k in args:
        print(k, args[k], end=' ', sep='->')
    if args:
        print()


def my_func3(*args, **kwargs) -> None:
    for a in args:
        print(a, end=' ')
    for (k, v) in kwargs.items():
        print(k, v, end=' ', sep='->')
    if args:
        print()

values1 = [1, 2, 3]
values2 = (4, 5, 6)
values3 = {7, 8, 9}
values4 = {'key1': 1, 'key2': 2, 'key3': 3, }

my_func()
my_func(values1)
my_func(*values1)
my_func(values2)
my_func(*values2)
my_func(values3)
my_func(*values3)
my_func(values4)
my_func(*values4)

my_func2()
my_func2(a=1, b=2)
my_func2(**values4)

my_func3()
my_func3(values1)
my_func3(*values1)
my_func3(values2)
my_func3(*values2)
my_func3(values3)
my_func3(*values3)
my_func3(values4)
my_func3(*values4)
my_func3(**values4)
my_func3(values1, **values4)
my_func3(values2, **values4)
my_func3(values3, **values4)
my_func3(*values1, **values4)
my_func3(*values2, **values4)
my_func3(*values3, **values4)