
file_name = input("Enter the name of the text file: ")


n = int(input("Enter the number of lines to read from the end: "))

try:
    
    with open(file_name, 'r') as file:
       
        all_lines = file.readlines()
        
        
        start_index = max(0, len(all_lines) - n)
        
        
        last_n_lines = all_lines[start_index:]
        
      
        print(f"Last {n} lines of the file:")
        for line in last_n_lines:
            print(line, end='')  
        
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
