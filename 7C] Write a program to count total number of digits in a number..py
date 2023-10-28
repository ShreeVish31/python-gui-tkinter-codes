
number_str = input("Enter a number: ")

digit_count = 0

for char in number_str:
    
    if char.isdigit():
        digit_count += 1


print(f"Total number of digits in the number: {digit_count}")
