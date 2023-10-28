previous_number = 0
current_number = 1

for i in range(10):    
    sum_of_numbers = previous_number + current_number
    
    print(f"The sum of {previous_number} and {current_number} is {sum_of_numbers}")
    
    previous_number, current_number = current_number, sum_of_numbers
