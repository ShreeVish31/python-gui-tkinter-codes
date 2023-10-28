try:
   
    filename = input("Enter the filename: ")
   
    with open(filename, 'r') as file:
        
        print(f"File '{filename}' opened successfully.")
        
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
