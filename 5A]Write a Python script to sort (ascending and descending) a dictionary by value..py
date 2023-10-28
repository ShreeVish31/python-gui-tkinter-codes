my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}


ascending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))


descending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))


print("Ascending order:")
print(ascending_sorted_dict)

print("\nDescending order:")
print(descending_sorted_dict)
