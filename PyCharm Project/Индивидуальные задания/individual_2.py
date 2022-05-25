#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    slov = input("Введите слово из 15 букв: ")
    if len(slov) != 15:
        print("Ошибка", file=sys.stderr)
        exit(1)

    k = int(input("Введите k: "))
    s = int(input("Введите s: "))
    if not 0 < k < s < 16:
        print("Ошибка", file=sys.stderr)
        exit(1)

    ch = list(slov)

    i = 0
    while k+i < s-2-i:
        dp = ch[k+i]
        ch[k+i] = ch[s-2-i]
        ch[s-2-i] = dp
        i += 1

    print(''.join(ch))