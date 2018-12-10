import pprint

def search4vowels(phrase:str) -> set:
    """Выводит гласные найденные во введенном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4leters(phrase:str, leters:str = 'aeiou') -> set:
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

count4vowels(input('Provide a word to search for vowels: '))