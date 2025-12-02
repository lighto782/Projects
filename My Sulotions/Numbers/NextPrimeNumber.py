'''
Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

primes = []
start = 3

print("The first prime nubmer is 2")

c = ''

while 1:
    isprime = True
    if c == 'y' or c == '':
        for i in primes:
            if start % i == 0:
                start += 2
                isprime = False
                break
        if isprime:
            print("Next is " + str(start))
            primes.append(start)
            c = input("Do you want to continue? (Y/n): ").strip().lower()
            start += 2
            
    else:
        print("The list:")
        print(primes)
        print("")
        print("K byeeee!")
        break

