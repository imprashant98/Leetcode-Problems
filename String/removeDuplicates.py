def remove_duplicates(string):
    stack = []  # Using a stack to store non-duplicate characters
    for char in string:
        if stack and char == stack[-1]:
            stack.pop()  # Remove the top element from the stack if it is a duplicate
        else:
            # Push the character onto the stack if it is not a duplicate
            stack.append(char)
    return ''.join(stack)  # Convert the stack to a string and return


# Test the function with the given input
S = "abccbccba"
output = remove_duplicates(S)
print("Output:", output)
