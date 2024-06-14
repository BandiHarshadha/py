def count_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
user_string = input("Enter a string: ")
result = count_characters(user_string)
for char, count in result.items():
    print(f"'{char}' occurs {count} times")
