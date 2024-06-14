def count_occurrences(lst, target):
    return lst.count(target)
my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_count = 2
result = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {result} times in the list.")
