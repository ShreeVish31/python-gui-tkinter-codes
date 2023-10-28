
input_string = "Hello, World!"

even_index_chars = ""


for i in range(0, len(input_string), 2):
    even_index_chars += input_string[i]


print("Characters at even indices:", even_index_chars)
