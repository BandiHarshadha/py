def calculate_sum(numbers):
    return sum(numbers)
try:
    num_list = [float(x) for x in input("Enter a list of numbers (separated by spaces): ").split()]
    total_sum = calculate_sum(num_list)
    print(f"The sum of the numbers is: {total_sum:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
