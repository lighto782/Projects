def ReturnChange(price: float, money: float) -> str:
    '''
    The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
    '''
    to_units = lambda x: int(round(x * 1000))
    
    price = to_units(price)
    money = to_units(money)
    
    due = money - price
    
    if due < 0:
        return "YOU DON'T HAVE ENOUGH MONEY YOU DUMBASS!"
    elif due == 0:
        return "Have a good day!"
    
    currency = [
        (50000,"Fifty Dinar"),
        (20000,"Twenty Dinar"),
        (10000,"Ten Dinar"),
        (5000,"Five Dinar"),
        (1000,"Dinar"),
        (500,"Fifty Qersh"),
        (250,"Quarter of Dinar"),
        (100,"Ten Qrosh"),
        (50,"Five Qrosh")
    ]
    
    result = []
    for value, name in currency:
        if value <= due:
            count = due // value
            due -= count * value
            result.append(f"{count} {name}")
            
    if due > 0:
        result.append(f"{due} Dirham (No coin available)")        

    if len(result) > 1:
        return ", ".join(result[:-1]) + " and " + result[-1]
    else:
        return result[0]

if __name__ == "__main__":
    try:
        price = float(input("Enter the price (LYD): "))
        money = float(input("Enter amount paid (LYD): "))
        print(ReturnChange(price, money))
    except ValueError:
        print("Please enter valid numbers.")