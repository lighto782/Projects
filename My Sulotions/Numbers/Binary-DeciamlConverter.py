
'''
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
'''

def BinaryToDecimal(b: str) -> float:
    g = b.split('.')
    powerP = 0
    powerN = -1
    decimal = 0.0
    for i in reversed(g[0]):
        if i == '0':
            powerP += 1
            continue
        elif i == '1':
            decimal += 2 ** powerP
            powerP += 1
        else:
            print("invalid input!")
            return None
    
    for i in g[1]:
        if i == '0':
            powerN -= 1
            continue
        elif i == '1':
            decimal += 2 ** powerN
            powerN -= 1
        else:
            print("invalid input!")
            return None
    
    return decimal


def DecimalToBinary(d: int) -> int:
    binary = []
    if d == 0:
        return 0
    else:
        while d > 0:
            binary.append(str(d%2))
            d = d // 2

        binary.reverse()
        return int("".join(binary))

if __name__ == "__main__":
    print("1.Binary to Decimal")
    print("2.Decimal to Binary")
    c = input("Enter 1 or 2: ")
    if c == '1':
        x = input("Enter the number to converted: ")
        print(BinaryToDecimal(x))
        
    elif c == '2':
        x = input("Enter the number to converted: ")
        print(DecimalToBinary(int(x)))
    else:
        print("Invalid input!")
        
# end main