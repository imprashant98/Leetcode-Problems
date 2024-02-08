def count_repeated_numbers(arr):
    num_count = {}

    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1

    repeated_numbers = {num: count for num,
                        count in num_count.items() if count > 1}

    return repeated_numbers


# Example usage:
arr = [1, 2, 3, 4, 2, 3, 5, 6, 7, 5, 8, 9, 9, 1, 10]
result = count_repeated_numbers(arr)
print(result)
