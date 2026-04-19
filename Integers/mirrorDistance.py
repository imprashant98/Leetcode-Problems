class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(x: int) -> int:
            rev = 0
            while x > 0:
                rev = rev * 10 + (x % 10)  # Get the last digit and add it to the reversed number
                x //= 10 # Remove the last digit from x using floor division
            return rev
        
        return abs(n - reverse(n))
    

#Example Usage 
solution_instance = Solution()
n = 556
result = solution_instance.mirrorDistance(n)
print(result) 