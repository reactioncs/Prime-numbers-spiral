# -*- coding: UTF-8 -*-

"""
generate prime numbers, stored in PN.txt
"""

import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def generate(upper_limit):
    with open("PN.txt", 'w') as f:
        f.write("2")
        for n in range(3, upper_limit):
            if isPrime(n):
                f.write(',' + str(n))


if __name__ == '__main__':
    generate(999999)
