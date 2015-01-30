"""
Docstring
"""
# Author:  Wiktor Matuszewski
# Created: 29-01-2015
# Version: 0.0.2

from slowa import NUMS, POWERS, ENDINGS, ZERO, CURRENCIES


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


def _pick_form(num, forms):
    if num >= 1000:
        return forms[2]
    last1, last2 = num % 10, num % 100
    if num == 1:
        idx = 0
    elif 2 <= last1 <= 4 and not 12 <= last2 <= 14:
        idx = 1
    else:
        idx = 2
    return forms[idx]


def slownie3(num):
    assert 0 <= num < 1000, 'I can only spell numbers between 0 and 999'
    return list(NUMS[idx] for idx in _decompose(num))


def num_slownie(num):
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

                if three == 1:
                    result.remove(NUMS[1])

                power = POWERS[thousands]
                ending = 1 if thousands == 1 else 2
                form = _pick_form(three, ENDINGS[ending])
                result.append(power.format(form))

        except KeyError:
            return 'zbyt wielka liczba'

    return ' '.join(result)


def slownie(num, currency=''):
    if isinstance(num, int):
        val = num_slownie(num)
        if not currency:
            return val
        curr = _pick_form(num, CURRENCIES[currency][0])
        return '{} {}'.format(val, curr)

    elif isinstance(num, float):
        if currency:
            snum = '{:.2f}'.format(num)
        else:
            snum = str(num)
            dec_places = len(snum.split('.')[1])
        left, right = snum.split('.')
        whole = num_slownie(int(left))
        dec_part = num_slownie(int(right))
        if not currency:
            return '{} i {} {}'.format(whole, dec_part, dec_places)
        curr_whole = _pick_form(int(left), CURRENCIES[currency][0])
        curr_decp = _pick_form(int(right), CURRENCIES[currency][1])
        return '{} {} i {} {}'.format(whole, curr_whole, dec_part, curr_decp)

    else:
        return 'Zły format liczby'



def main():
    print(slownie(100001))


if __name__ == '__main__':
    main()
