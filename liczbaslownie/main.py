"""
Docstring
"""
# Author:  Wiktor Matuszewski
# Created: 29-01-2015
# Version: 0.0.2

from slowa import NUMS, POWERS, ENDINGS, ZERO


def _append_non_zero(list_, elt):
    if elt:
        list_.append(elt)


def _decompose(num):
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
    return list(NUMS[idx] for idx in _decompose(num))


def slownie(num):
    try:
        num = int(num)
    except ValueError:
        return 'Błąd: zły format liczby'

    if num == 0:
        return ZERO

    threes = []
    while num:
        threes.append(num % 1000)
        num //= 1000

    result = []
    while threes:
        # budowanie wyniku trójkami - od lewej do prawej
        three = threes.pop()
        thousands = len(threes)
        result.extend(slownie3(three))

        try:
            # wybór słowa 'tysiące', 'miliony' itp. i odpowiedniej końcówki
            if threes and three != 0:

                last1, last2 = three % 10, three % 100

                if three == 1:
                    form = 0
                    result.remove(NUMS[1])
                elif 2 <= last1 <= 4 and not 12 <= last2 <= 14:
                    form = 1
                else:
                    form = 2

                power = POWERS[thousands]
                ending = 1 if thousands == 1 else 2
                result.append(power.format(ENDINGS[ending][form]))

        except KeyError:
            return 'zbyt wielka liczba'

    return ' '.join(result)


def main():
    print(slownie(100001))


if __name__ == '__main__':
    main()
