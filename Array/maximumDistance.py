from typing import List
import bisect

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter = 4 * side

        def to_1d(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 2 * side + (side - x)
            else:
                return 3 * side + (side - y)

        positions = sorted(to_1d(x, y) for x, y in points)
        n = len(positions)
        doubled = positions + [p + perimeter for p in positions]
        N = 2 * n
        LOG = k.bit_length()  # We need at most k-1 jumps

        def can_place(d: int) -> bool:
            # nxt[i] = next index reachable from i with gap >= d
            nxt = [
                bisect.bisect_left(doubled, doubled[i] + d, i + 1)
                for i in range(N)
            ]

            # Binary lifting table: lift[j][i] = index after 2^j jumps from i
            lift = [nxt[:]]  # lift[0] = nxt
            for j in range(1, LOG + 1):
                prev = lift[j - 1]
                curr = [0] * N
                for i in range(N):
                    p = prev[i]
                    curr[i] = prev[p] if p < N else N
                lift.append(curr)

            # For each start, apply k-1 jumps using binary lifting
            for start in range(n):
                idx = start
                valid = True
                remaining = k - 1

                j = LOG
                while j >= 0:
                    if remaining >= (1 << j):
                        idx = lift[j][idx]
                        remaining -= (1 << j)
                        if idx >= start + n:
                            valid = False
                            break
                    j -= 1

                if valid and idx < start + n:
                    # Wrap-around check
                    if doubled[start] + perimeter - doubled[idx] >= d:
                        return True

            return False

        lo, hi = 1, perimeter // k
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans