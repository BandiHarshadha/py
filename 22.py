def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)
my_list = [10, 5, 8, 3, 12, 7]
min_val, max_val = find_min_max(my_list)

print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")
