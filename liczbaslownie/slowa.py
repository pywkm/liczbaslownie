"""
Polish representation of numbers (integers, floats, currencies, etc.)
Słowne przedstawienie liczb (całkowitych, )
"""
# Author:  Wiktor Matuszewski
# Created: 28-01-2015
# Version: 0.0.1a


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


_base = (
    '{}', 'dw{}', 'trzy{}', 'czter{}', 'pięć{}',
    'sześć{}', 'siedem{}', 'osiem{}', 'dziewięć{}',
    )
ZERO = {0: 'zero'}
DIGITS = _compose(1, 1, _base, ['jeden', 'a', '', 'y'] + ['']*5)
TEENS = _compose(11, 1, _cut_sc(_base), ['jedenaście', 'anaście'] + ['naście']*7)
TENS = _compose(
    10,
    10,
    _base,
    ['dziesięć', 'adzieścia'] + ['dzieści']*2 + ['dziesiąt']*5,
    )
HUNDREDS = _compose(100, 100, _base, ['sto', 'ieście', 'sta', 'ysta'] + ['set']*5)

_all = {}
for dict_ in (ZERO, DIGITS, TEENS, TENS, HUNDREDS):
    _all.update(dict_)
ALL = dict(_all)
del _all
