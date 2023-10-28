
input_string = input("Enter a string: ")


if len(input_string) >= 2:

    result_string = input_string[:2] + input_string[-2:]
    print("Result:", result_string)
else:
    print("String length is less than two, returning an empty string.")
