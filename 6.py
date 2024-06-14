
file_name = "user_input.txt"

try:
  
    with open(file_name, "r") as file:
        content = file.read()
        print(f"Content of {file_name}:\n{content}")
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please make sure the file exists.")
