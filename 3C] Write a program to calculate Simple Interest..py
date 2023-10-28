def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per year (%): "))
time = float(input("Enter the time period (in years): "))

if principal < 0 or time < 0 or rate <= 0:
    print("Please enter valid values. Principal and time should be non-negative, and rate should be positive.")
else:
    interest = calculate_simple_interest(principal, rate, time)
    print(f"The Simple Interest is: {interest}")
