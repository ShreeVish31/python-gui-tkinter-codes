class EvenNumberError(Exception):
    pass

class OddNumberError(Exception):
    pass

def check_even_or_odd(number):
    if number % 2 == 0:
        raise EvenNumberError("Even numbers are not allowed.")
    else:
        raise OddNumberError("Odd numbers are not allowed.")

try:
    user_input = int(input("Enter a number: "))
    check_even_or_odd(user_input)
    print("Input is neither even nor odd.")
except EvenNumberError as e:
    print(f"Error: {e}")
except OddNumberError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
