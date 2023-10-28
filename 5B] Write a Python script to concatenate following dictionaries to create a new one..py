
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}


concatenated_dict1 = dict1.copy()  
concatenated_dict1.update(dict2)   
concatenated_dict1.update(dict3)   


concatenated_dict2 = {**dict1, **dict2, **dict3}


print("Concatenated dictionary (Method 1):")
print(concatenated_dict1)

print("\nConcatenated dictionary (Method 2):")
print(concatenated_dict2)
