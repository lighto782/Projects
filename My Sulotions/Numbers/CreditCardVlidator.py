'''
Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discover) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).
'''

def CardValidator(number) -> bool:
    number = number.replace(' ','')[::-1]
    
    number = [int(i) for i in number]
    
    for x in range(1, len(number),2):
        number[x] *= 2
        if number[x] > 9:
            number[x] = number[x] % 10 + 1
            
    total = sum(number)
    return total % 10 == 0    

if __name__ == "__main__":
    card = input("Enter your card: ")
    print(CardValidator(card))