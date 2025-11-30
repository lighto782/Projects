import math
import time

'''
Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''



def factor(n):
    factors = []
    i = 2
    m = n
    ts = time.time()
    while i <= int(n/2):
        if m % i == 0:
            m = int(m / i)
            factors.append(i)
            continue
        i += 1
    te = time.time()
    print("\nTime: " + str(te - ts) +"\n")
    if len(factors) > 0:
        return factors
    else:
        return "Number is prime and does not have prime factors!"

x = int(input("Enter the number you want to be factorized: "))

print(factor(x))