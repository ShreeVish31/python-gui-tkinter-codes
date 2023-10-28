try:
    
    input1 = input("Enter the first number: ")
    
   
    input2 = input("Enter the second number: ")
    
    
    num1 = float(input1)
    num2 = float(input2)
    
    
    result = num1 + num2
    
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter numerical values.")
except TypeError:
    print("Error: Invalid input. Please enter numerical values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
