#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    s = input("Введите текст: ").split(' ')
    wr = []

    for i in s:
        if i == s[0]:
            s.remove(i)

    for i in s:
        p = 0
        for k, item in enumerate(i):
            if i[k] in i[:k]:
                p += 1
        if p == 0:
            wr.append(i)

        q = 0
        for k,item in enumerate(i):
            if i[k] != i[-k - 1]:
                q += 1
        if q == 0:
            wr.append(i)

    wr = ', '.join(wr)
    print(wr)