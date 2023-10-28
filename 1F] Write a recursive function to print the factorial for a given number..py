def factorial(n):
   
    if n == 0:
        return 1
    else:
        
        result = n * factorial(n - 1)
        return result


user_number = int(input("Enter a number to calculate its factorial: "))


if user_number < 0:
    print("Factorial is not defined for negative numbers.")
else:
   
    fact = factorial(user_number)
    print(f"The factorial of {user_number} is {fact}")
