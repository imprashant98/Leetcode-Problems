from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # If the current asteroid moves to the right, just add it to the stack
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # If the current asteroid moves to the left:
                # 1. Pop asteroids moving to the right and smaller than the current asteroid
                # 2. Handle collision when necessary
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()

                # Handle the case where a collision occurs
                if stack and stack[-1] > 0 and stack[-1] == abs(asteroid):
                    stack.pop()  # Destroy both asteroids
                elif not stack or stack[-1] < 0:
                    # Keep the asteroid moving to the left
                    stack.append(asteroid)

        return stack


# Example usage:
solution = Solution()
asteroids = [5, 10, -5]
print(solution.asteroidCollision(asteroids))  # Output: [5, 10]
