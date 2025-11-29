from decimal import Decimal, getcontext
from math import factorial,e

'''
Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go
'''

getcontext().prec = 1000

n = int(input("Enter the numbers of digits for e: "))

def calce(x):
    e = Decimal(0)
    
    for i in range(x):
        e+= Decimal(1) / Decimal(factorial(i))
    return e

ee = calce(n)
print(ee)
