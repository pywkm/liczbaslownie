"""
Entry point
"""
# Author:  Wiktor Matuszewski
# Created: 29-01-2015
# Last changed: 10-02-2016
# Version: 0.0.3

from .slowa import NUMS, POWERS, ENDINGS, ZERO, CURRENCIES, AFTER_COMA


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


def _pick_form(num, forms, curr=False):
    if num >= 1000 and not curr:
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


def cz_dzies_slownie(snum):
    max_depth = max(AFTER_COMA.keys())
    snum = snum[:max_depth]
    while snum.endswith('0'):
        snum = snum[:-1]
    dec_part = num_slownie(int(snum))
    dec_places = len(snum)
    dec_places = max_depth if dec_places > max_depth else dec_places
    if dec_part == 'zero':
        return ''
    form = 2
    if dec_part == 'jeden':
        dec_part = 'jedna'
        form = 0
    elif dec_part.endswith(' dwa'):
        dec_part = dec_part[:-4] + ' dwie'
        form = 1
    elif snum.endswith('3') or snum.endswith('4'):
        form = 1
    return dec_part + ' ' + AFTER_COMA[dec_places][form]


def slownie(num, currency=''):
    if isinstance(num, int):
        val = num_slownie(num)
        if not currency:
            return val
        curr = _pick_form(num, CURRENCIES[currency][0], True)
        return '{} {}'.format(val, curr)

    elif isinstance(num, float):
        if currency:
            snum = '{:.2f}'.format(num)
        else:
            snum = str(num)
        left, right = snum.split('.')
        whole = num_slownie(int(left))
        if not currency:
            dec_part = cz_dzies_slownie(right)
            if dec_part:
                return '{} i {}'.format(whole, dec_part)
            else:
                return whole
        dec_part = num_slownie(int(right))
        curr_whole = _pick_form(int(left), CURRENCIES[currency][0], True)
        curr_decp = _pick_form(int(right), CURRENCIES[currency][1], True)
        return '{} {} i {} {}'.format(whole, curr_whole, dec_part, curr_decp)

    elif isinstance(num, str):
        try:
            num = float(num.replace(',', '.'))
            return slownie(num, currency)
        except ValueError:
            pass

    else:
        return 'Zły format liczby'


def main():
    print(slownie('12,345'))


if __name__ == '__main__':
    main()
