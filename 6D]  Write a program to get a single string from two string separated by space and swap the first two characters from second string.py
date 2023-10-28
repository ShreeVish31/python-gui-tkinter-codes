input_strings = input("Enter two strings separated by a space: ").split()


if len(input_strings) != 2:
    print("Please enter exactly two strings separated by a space.")
else:
   
    string1, string2 = input_strings

 
    if len(string1) >= 2 and len(string2) >= 2:
        
        new_string1 = string2[:2] + string1[2:]
        new_string2 = string1[:2] + string2[2:]

     
        result_string = new_string1 + " " + new_string2

        
        print("Swapped strings:", result_string)
    else:
        print("Both strings must have at least 2 characters.")
