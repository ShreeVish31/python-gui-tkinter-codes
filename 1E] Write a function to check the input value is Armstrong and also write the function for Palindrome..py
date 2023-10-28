def is_armstrong_number(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
   
    return armstrong_sum == number


user_number = int(input("Enter a number to check for Armstrong: "))


if is_armstrong_number(user_number):
    print(f"{user_number} is an Armstrong number.")
else:
    print(f"{user_number} is not an Armstrong number.")
def is_palindrome(input_string):
    
    input_string = input_string.replace(" ", "").lower()
    
   
    return input_string == input_string[::-1]


user_input = input("Enter a string to check for Palindrome: ")


if is_palindrome(user_input):
    print(f"{user_input} is a Palindrome.")
else:
    print(f"{user_input} is not a Palindrome.")
