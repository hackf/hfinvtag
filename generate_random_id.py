from sys import argv
from random import randint

numerals = '0123456789abcdefghijklmnopqrstuvwxyz'
b = len(numerals)

l = int(argv[1])
try:
    t = int(argv[2])
except IndexError:
    t = 1

def base(n):
    return ((n == 0) and numerals[0]) or \
           (base(n // b).lstrip(numerals[0]) + numerals[n % b])

for _ in range(t):
    print(base(randint(int('1' + '0' * (l - 1), b), int('z' * l, b))))
