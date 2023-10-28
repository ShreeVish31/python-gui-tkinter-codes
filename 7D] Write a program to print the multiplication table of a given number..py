number = int(input("Enter a number: "))

table_range = 10


print(f"Multiplication table for {number}:")

for i in range(1, table_range + 1):
    product = number * i
    print(f"{number} x {i} = {product}")
