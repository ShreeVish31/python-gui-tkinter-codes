def generate_square_list():
    
    square_list = []

    for num in range(1, 31):
        square = num ** 2
        square_list.append(square)

    return square_list


squares = generate_square_list()


print(squares)
