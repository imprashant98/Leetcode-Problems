# mock picked number
picked = 6

def guess(num: int) -> int:
    if num > picked:
        return -1
    elif num < picked:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid + 1


# example run
print(Solution().guessNumber(10))  # Output: 6