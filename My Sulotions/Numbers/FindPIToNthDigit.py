from math import factorial, sqrt
from decimal import Decimal, getcontext

'''
Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
'''


getcontext().prec=500

n = int(input("ENTER: "))

def calc(x):
    up = Decimal(0)
    down = Decimal(0)
    pi = Decimal(0)
    
    for i in range(n):
        up = (-1**i) * factorial(6*i) * (545140134*i+13591409)
        down = factorial(3*i) * factorial(i)**3 * 640320**(3*i)
        pi +=Decimal(up) /Decimal(down)
    pi = pi * (Decimal(1)/(Decimal(426880)*Decimal(sqrt(10005))))
    pi = 1 / pi
    return pi

print(calc(n))