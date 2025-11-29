'''
 Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

x = int(input("Enter the number: "))

print(fibonacci(x))