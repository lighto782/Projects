'''
A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
'''

def FindHappyNumber():
    for i in range(100000):
        n = i
        s = 0
        loop = []
        while s not in loop:
            loop.append(s)
            s = sum([int(x)**2 for x in str(n)])
            if s == 1:
                yield i
                break
            n = s

if __name__ == "__main__":
    happy_generator = FindHappyNumber()
    print("Finding happy numbers...")
    print(f"1. {next(happy_generator)}")
    i = 2
    while True:
        c = input("Do you want to continue (Y/n):")
        if c.lower() == "y"  or c == "":
            print("Finding happy numbers...")
            print(f"{i}. {next(happy_generator)}")
            i += 1
        else:
            break
    print("Done!")