import math 

# This program tells us if a given number is prime or not
user_input = input('Enter a positive integer greater than or equal to two: ')

try:
    number = int(user_input)
    #two is a prime number
    if number == 2:
        print('Prime number!')
    elif number > 2:
        prime = True
        divider = 2

        # OPTIMIZATION:
        # If a number is not prime, it must have two factors (a * b = number).
        # If both factors were greater than the square root, their product would exceed the number.
        # Therefore, at least one factor must be less than or equal to the square root.
        # Testing divisors up to this limit is mathematically sufficient and saves processing time.
        
        # Calculate the maximum limit ONLY ONCE before the loop begins
        limit = math.isqrt(number)
        
        # The loop now stops when the divider reaches the square root
        while divider <= limit and prime == True:
            if number % divider == 0:
                prime = False
            divider += 1
            
        if prime == True:
            print('Prime number!')
        else:
            print('Not a prime number!')
    else:
        print('Error: The number must be 2 or greater.')

except ValueError:
    print("Error: Invalid input. Please enter a whole number, not text.")