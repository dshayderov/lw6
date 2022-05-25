#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    s = input("Введите предложение: ")
    if "а" not in s and "о" not in s:
        print(
            "В предложении нет нужных букв",
            file=sys.stderr
        )
        exit(1)

    a = s.count("а")
    o = s.count("о")

    if a > o:
        print("Буква 'а' встречается в предложении чаще")
    elif o > a:
        print("Буква 'о' встречается в предложении чаще")
    else:
        print("Буквы встречаются одинаковое кол-во раз")