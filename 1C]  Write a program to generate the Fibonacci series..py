n = int(input("Enter the number of Fibonacci terms to generate: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci Series:")
    print(a)
else:
    
    print("Fibonacci Series:")
    print(a)
    print(b)
    for _ in range(2, n):
        
        next_term = a + b
      
        print(next_term)
       
        a, b = b, next_term
