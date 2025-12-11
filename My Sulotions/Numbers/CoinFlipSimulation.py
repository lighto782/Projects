'''
Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
'''

from random import random

def flipCoin() -> bool:
    return True if random() > 0.5 else False

if __name__ == "__main__":
    x = input("How many times you want to flip the coin?: ")
    heads = 0
    tails = 0
    for i in range(int(x)):
        if flipCoin():
            heads += 1
        else:
            tails += 1
    print("You got %d heads and %d tails, the ratio is %.2f%%" % (heads, tails, heads/int(x) * 100))