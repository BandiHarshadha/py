
user_input = input("Enter a string: ")
file_name = "user_input.txt"
with open(file_name, "w") as file:
    file.write(user_input)

print(f"String '{user_input}' has been written to {file_name}")
