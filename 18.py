def are_anagrams(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()


    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)


    return sorted_str1 == sorted_str2
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
