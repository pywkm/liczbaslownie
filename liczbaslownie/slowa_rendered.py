"""
Polish representation of numbers (integers, floats, currencies, etc.)
Słowne przedstawienie liczb (całkowitych, zmiennoprzecinkowych, walut)
"""
# Author:  Wiktor Matuszewski
# Created: 28-01-2015
# Last changed: 10-02-2016
# Version: 0.0.3


POWERS = {
    1: 'tys{}', 2: 'milion{}', 3: 'miliard{}',
    4: 'bilion{}', 5: 'biliard{}', 6: 'trylion{}',
    7: 'tryliard{}', 8: 'kwadrylion{}', 9: 'kwadryliard{}',
    10: 'kwintylion{}', 11: 'kwintyliard{}', 12: 'sekstylion{}',
    13: 'sekstyliard{}', 14: 'septylion{}', 15: 'septyliard{}',
    16: 'oktylion{}', 17: 'oktyliard{}', 18: 'nonylion{}',
    19: 'nonyliard{}', 20: 'decylion{}', 21: 'decyliard{}',
    22: 'undecylion{}', 23: 'undecyliard{}', 24: 'duodecylion{}',
    25: 'duodecyliard{}',
    }

ENDINGS = {
    1: ('iąc', 'iące', 'ięcy'),
    2: ('', 'y', 'ów'),
    }

NUMS = {
    1: 'jeden',
    2: 'dwa',
    3: 'trzy',
    4: 'cztery',
    5: 'pięć',
    6: 'sześć',
    7: 'siedem',
    8: 'osiem',
    9: 'dziewięć',
    10: 'dziesięć',
    11: 'jedenaście',
    12: 'dwanaście',
    13: 'trzynaście',
    14: 'czternaście',
    15: 'piętnaście',
    16: 'szesnaście',
    17: 'siedemnaście',
    18: 'osiemnaście',
    19: 'dziewiętnaście',
    20: 'dwadzieścia',
    30: 'trzydzieści',
    40: 'czterdzieści',
    50: 'pięćdziesiąt',
    60: 'sześćdziesiąt',
    70: 'siedemdziesiąt',
    80: 'osiemdziesiąt',
    90: 'dziewięćdziesiąt',
    100: 'sto',
    200: 'dwieście',
    300: 'trzysta',
    400: 'czterysta',
    500: 'pięćset',
    600: 'sześćset',
    700: 'siedemset',
    800: 'osiemset',
    900: 'dziewięćset',
    }

ZERO = 'zero'
