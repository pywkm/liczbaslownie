"""
Docstring
"""
# Author:  Wiktor Matuszewski
# Created: 29-01-2015
# Version: 0.0.1a

from slowa import ALL

def _append_non_zero(list_, elt):
    if elt:
        list_.append(elt)


def decompose(num):
    assert num < 1000, 'I can only decompose numbers between 0 and 999'
    result = []
    hundreds = (num // 100) * 100
    _append_non_zero(result, hundreds)
    tens = ((num - hundreds) // 10) * 10
    tens = 0 if tens < 20 else tens
    _append_non_zero(result, tens)
    rest = num - hundreds - tens
    _append_non_zero(result, rest)
    return result


def slownie3(num):
    assert 0 <= num < 1000, 'I can only spell numbers between 0 and 999'
    return ' '.join(ALL[idx] for idx in decompose(num))


def main():
    # print(ALL)
    print(decompose(820))
    print(slownie3(820))


if __name__ == '__main__':
    main()
