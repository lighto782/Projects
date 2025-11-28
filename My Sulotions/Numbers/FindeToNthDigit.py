from decimal import Decimal, getcontext
from math import factorial,e
getcontext().prec = 1000

n = int(input("Enter the numbers of digits for e: "))

def calce(x):
    e = Decimal(0)
    
    for i in range(x):
        e+= Decimal(1) / Decimal(factorial(i))
    return e

ee = calce(n)
print(ee)
