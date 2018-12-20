import pprint


def search4vowels(phrase: str) -> set:
    """Выводит гласные найденные во введенном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4leters(phrase: str, leters: str = 'aeiou') -> set:
    """Возвращает множество букв из 'leters', найденных в указанной фразе."""
    return set(leters).intersection(set(phrase))


def count4vowels(phrase):
    """Выводит гласные найденные во введенном слове"""
    vowels = set('aeiou')
    r = {}
    for c in list(phrase):
        if c not in vowels:
            continue
        r.setdefault(c, 0)
        r[c] += 1
    pprint.pprint(r)
    return bool(r)


def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


var1 = [1]
double(var1)
print(var1)

var2 = ['data']
change(var2)
print(var2)
