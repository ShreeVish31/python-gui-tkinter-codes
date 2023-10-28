import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = 2023
years_until_100 = 100 - age
year_of_turning_100 = current_year + years_until_100

print(f"Hello, {name}! You will turn 100 years old in the year {year_of_turning_100}.")




or



import datetime 
name = input("Hello! Please enter your name: ") 
print("Hello " + name) 
age = int(input("Enter your age: ")) 
year_now = datetime.datetime.now() 
# print(year_now.year) 
print("You will turn 100 in " + str(int(100-age) + int(year_now.year))) 
