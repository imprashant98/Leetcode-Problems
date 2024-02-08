def reverseVowelsString(s):
    vowels = ""
    for char in s:
        if char in "aeiouAEIOU":
            vowels += char
    result_string = ""
    for char in s:
        if char in "aeiouAEIOU":
            result_string += vowels[-1]
            vowels = vowels[:-1]
        else:
            result_string += char
    return result_string


print(reverseVowelsString("JavaTpoint"))
