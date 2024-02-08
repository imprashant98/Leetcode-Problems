def second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"

    first_max = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])

    for num in arr[2:]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    return second_max


# Example usage:
arr = [3, 7, 1, 9, 5, 4]
result = second_largest(arr)
print(result)  # Output: 7 (since 7 is the second largest element in the array)
