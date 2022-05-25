#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    s = input("Введите предложение: ")
    ls = []

    for x in s:
        if x.isdigit():
            ls.append(x)

    ls = ', '.join(ls)
    print(ls)