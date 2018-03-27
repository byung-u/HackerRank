#!/usr/bin/env python3
from math import floor

NUMBER_WORDS = { 1: "One",
                 2: "Two",
                 3: "Three",
                 4: "Four",
                 5: "Five",
                 6: "Six",
                 7: "Seven",
                 8: "Eight",
                 9: "Nine",
                 10: "Ten",
                 11: "Eleven",
                 12: "Twelve",
                 13: "Thirteen",
                 14: "Fourteen",
                 15: "Fifteen",
                 16: "Sixteen",
                 17: "Seventeen",
                 18: "Eighteen",
                 19: "Nineteen",
                 20: "Twenty",
                 30: "Thirty",
                 40: "Forty",
                 50: "Fifty",
                 60: "Sixty",
                 70: "Seventy",
                 80: "Eighty",
                 90: "Ninety"}


def number_to_word(n):
    english_parts = []
    ones = n % 10
    tens = n % 100
    hundreds = floor(n / 100) % 10
    thousands = floor(n / 1000)

    if thousands:
        english_parts.append(number_to_word(thousands))
        english_parts.append('Thousand')
        # if not hundreds and tens:
        #     english_parts.append('And')
    if hundreds:
        english_parts.append(NUMBER_WORDS[hundreds])
        english_parts.append('Hundred')
        # if tens:
        #     english_parts.append('And')
    if tens:
        if tens < 20 or ones == 0:
            english_parts.append(NUMBER_WORDS[tens])
        else:
            english_parts.append(NUMBER_WORDS[tens - ones])
            english_parts.append(NUMBER_WORDS[ones])
    return ' '.join(english_parts)


def ntow(n):
    r = None
    result = []
    if n == 1000000000000:
        return 'One Trillion'
    if n > 10 ** 9:
        r = floor(n / (10 ** 9))
        n = n % (10 ** 9)
        result.append(number_to_word(r))
        result.append('Billion')
    if n > 10 ** 6:
        r = floor(n / (10 ** 6))
        n = n % (10 ** 6)
        result.append(number_to_word(r))
        result.append('Million')
    if n > 10 ** 3:
        r = floor(n / (10 ** 3))
        n = n % (10 ** 3)
        result.append(number_to_word(r))
        result.append('Thousand')

    result.append(number_to_word(n))
    return ' '.join(result)

for _ in range(int(input())):
    n = int(input())
    print(ntow(n))
