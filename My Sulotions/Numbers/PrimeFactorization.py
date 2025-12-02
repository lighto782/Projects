import math

def get_prime_factors(n: int) -> list[int]:
    """
    Finds all prime factors of a number n.
    Returns a list of integers.
    """
    factors = []
    
    # Handle 2 separately to allow skipping even numbers in the loop
    while n % 2 == 0:
        factors.append(2)
        n //= 2  # Use integer division
        
    # Loop from 3 up to sqrt(n), skipping even numbers
    # We check i*i <= n instead of calculating sqrt each time
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
        
    # If n is still > 1, it means the remaining n is a prime itself
    if n > 1:
        factors.append(n)
        
    return factors

if __name__ == "__main__":
    try:
        num_input = int(input("Enter the number you want to be factorized: "))
        if num_input < 2:
            print("Please enter a number greater than 1.")
        else:
            result = get_prime_factors(num_input)
            # If list has 1 element matching input, it was prime
            if len(result) == 1 and result[0] == num_input:
                print(f"{num_input} is prime!")
            else:
                print(f"Prime factors: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
