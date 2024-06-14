
main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")
if substring in main_string:
    print(f"'{substring}' is present in the main string.")
else:
    print(f"'{substring}' is not found in the main string.")
