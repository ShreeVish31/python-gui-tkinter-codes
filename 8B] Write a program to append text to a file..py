
file_name = input("Enter the name of the text file to which you want to append: ")

try:
    
    with open(file_name, 'a') as file:
        
        text_to_append = input("Enter the text to append: ")
        
       
        file.write(text_to_append + '\n')  
        
        print("Text appended successfully.")
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    
