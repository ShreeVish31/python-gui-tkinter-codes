try:
    user_input = input("Please enter an integer: ")
    num = int(user_input)
    print(f"You entered: {num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
