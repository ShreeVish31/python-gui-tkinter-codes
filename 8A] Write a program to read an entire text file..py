
file_name = input("Enter the name of the text file: ")

try:
    
    with open(file_name, 'r') as file:
        
        file_contents = file.read()
        
       
        print("Contents of the file:")
        print(file_contents)
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
