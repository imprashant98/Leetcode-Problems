class Solution:
    def sequentialDigits(self, low, high):
        result = []
        digits = "123456789"

        low_length, high_length = len(str(low)), len(str(high))

        for length in range(low_length, high_length + 1):
            for i in range(10 - length):
                num_str = digits[i:i + length]
                num = int(num_str)
                if low <= num <= high:
                    result.append(num)

        return result


# Example usage:
# Create an instance of the Solution class
solution_instance = Solution()

# Example 1
low1, high1 = 100, 300
output1 = solution_instance.sequentialDigits(low1, high1)
print(output1)  # Output: [123, 234]

# Example 2
low2, high2 = 1000, 13000
output2 = solution_instance.sequentialDigits(low2, high2)
print(output2)  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]
