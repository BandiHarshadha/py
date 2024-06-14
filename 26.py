def check_prefix_suffix(input_string, prefix, suffix):
    return input_string.startswith(prefix) or input_string.endswith(suffix)
user_string = input("Enter a string: ")
user_prefix = input("Enter a prefix: ")
user_suffix = input("Enter a suffix: ")
if check_prefix_suffix(user_string, user_prefix, user_suffix):
    print("The string meets the specified conditions.")
else:
    print("The string does not meet the specified conditions.")
