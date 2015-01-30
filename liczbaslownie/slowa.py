"""
Polish representation of numbers (integers, floats, currencies, etc.)
Słowne przedstawienie liczb (całkowitych, )
"""
# Author:  Wiktor Matuszewski
# Created: 28-01-2015
# Version: 0.0.2


_powers = {1: 'tys{}'}

_prefixes = {
    2: 'mi{}', 4: 'bi{}', 6: 'try{}',
    8: 'kwadry{}', 10: 'kwinty{}', 12: 'seksty{}',
    14: 'septy{}', 16: 'okty{}', 18: 'nony{}',
    20: 'decy{}', 22: 'undecy{}', 24: 'duodecy{}',
    }

for n in _prefixes:
    _powers[n] = _prefixes[n].format('lion{}')
    _powers[n+1] = _prefixes[n].format('liard{}')

POWERS = dict(_powers)

ENDINGS = {
    1: ('iąc', 'iące', 'ięcy'),
    2: ('', 'y', 'ów'),
    }

CURRENCIES = {
    'zł': ('złoty', 'złote', 'złotych'),
    'gr': ('grosz', 'grosze', 'groszy'),
    }

def _compose(start, step, base, endings):
    result = {}
    idx = start
    for i, s in enumerate(base):
        result[idx] = s.format(endings[i])
        idx += step
    return result


def _cut_sc(strings):
    names = []
    for name in strings:
        name = name.replace('ść', 's')
        name = name.replace('ć', 't')
        names.append(name)
    return tuple(names)


ZERO = 'zero'

_base = (
    '{}', 'dw{}', 'trzy{}', 'czter{}', 'pięć{}',
    'sześć{}', 'siedem{}', 'osiem{}', 'dziewięć{}',
    )
d1_9 = _compose(1, 1, _base, ['jeden', 'a', '', 'y'] + ['']*5)
d11_19 = _compose(11, 1, _cut_sc(_base), ['jedenaście', 'anaście'] + ['naście']*7)
d10_90 = _compose(
    10,
    10,
    _base,
    ['dziesięć', 'adzieścia'] + ['dzieści']*2 + ['dziesiąt']*5,
    )
d100_900 = _compose(100, 100, _base, ['sto', 'ieście', 'sta', 'ysta'] + ['set']*5)

_all = {}
for d in (d1_9, d11_19, d10_90, d100_900):
    _all.update(d)

NUMS = dict(_all)
del _all
