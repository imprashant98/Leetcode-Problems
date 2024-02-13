def cipher(s, key):
    if key <= 1:
        return s

    # Initialize a list of empty strings for each row
    rows = [''] * key
    current_row = 0
    direction = 1

    for char in s:
        rows[current_row] += char
        # Change direction when reaching the top or bottom row
        if current_row == 0:
            direction = 1
        elif current_row == key - 1:
            direction = -1
        current_row += direction

    # Concatenate all rows to form the ciphered string
    return ''.join(rows)


# Test the function
s = "YOUCANTSEEME"
key = 2
print(cipher(s, key))  # Output: "YUATEMOCNSEE"
