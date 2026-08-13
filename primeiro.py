#this program will tell you if a number is divisible by nine 
user_input = input("Enter a number:")
try:
    #now the program try to convert the string to a number
    number = int(user_input)
    #if the rest of the division of the number by nine is zero, then tihis number is divisible by nine
    if number%9 == 0:
        print('Divisible by 9.')
    else:
        print('Not divisible by 9.')

except ValueError:
    #if the program fail in convert, than show an error massage to user
    print("Error: Invalid input. Please enter an integer, not text.")