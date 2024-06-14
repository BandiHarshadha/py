import string
def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string
user_string = input("Enter a string: ")
result = remove_punctuation(user_string)
print(f"The string without punctuation: {result}")
