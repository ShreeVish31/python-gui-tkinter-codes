def remove_elements_by_indices(input_list, indices_to_remove):
   
    result_list = [input_list[i] for i in range(len(input_list)) if i not in indices_to_remove]
    return result_list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


indices_to_remove = [0, 2, 4, 5]


new_list = remove_elements_by_indices(my_list, indices_to_remove)


print(new_list)
