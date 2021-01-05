#!usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt
from time import sleep

time = list()
lengths = list()
err_lst = set()
start = datetime.now()


def passwords_length(error, tm, le, t):
    """Add len values to list"""
    print('Установите набор предполагаемых длин пароля, вводите через пробел \nчто бы завершить ввод нажмите Enter\n')
    sleep(2.0)
    ln_lst = [int(i) for i in input('Введите несколько чисел: ').split()]
    return brute_force_table(ln_lst, error, tm, le, t)


def brute_force_value(length, tm, error, le, t):
    val = np.random.randint(0, 10, size=length[0])
    return compare(error, tuple(val), tm, le, t, length)


def brute_force_table(length, error, tm, le, t):
    while len(length) != 0:
        while len(error) != int('9' * length[0]):
            error.add(tuple(np.random.randint(0, 10, size=length[0])))
        print('Таблица сформирована за: ', datetime.now() - tm)
        return brute_force_value(length, tm, error, le, t)
    return visualisation(le, t)


def compare(error, real_p, tm, le, t, length):
    if real_p in error:
        end = datetime.now()-tm
        t.append(str(end))
        le.append(len(real_p))
        error.clear()
        length.remove(length[0])
        return brute_force_table(length, error, start, le, t)
    else:
        return print('Need recursion')


def visualisation(le, t):
    plt.plot(t, le, color='green', linestyle='solid', label='progression')
    return plt.show()


passwords_length(err_lst, start, lengths, time)
