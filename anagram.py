def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)


# Test the function
string1 = "tac"
string2 = "act"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")