from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF_NEG = -(10**9)

        # dp for previous row and current row
        dp_prev = [[INF_NEG] * (k + 1) for _ in range(n)]
        dp_cur = [[INF_NEG] * (k + 1) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                # start cell
                if i == 0 and j == 0:
                    cost = 1 if grid[0][0] > 0 else 0
                    if cost <= k:
                        dp_cur[0][cost] = grid[0][0]
                    continue

                cell_cost = 1 if grid[i][j] > 0 else 0
                cell_score = grid[i][j]

                # from top (i-1, j)
                if i > 0:
                    for c in range(k + 1):
                        if dp_prev[j][c] > INF_NEG:
                            nc = c + cell_cost
                            if nc <= k:
                                ns = dp_prev[j][c] + cell_score
                                if ns > dp_cur[j][nc]:
                                    dp_cur[j][nc] = ns

                # from left (i, j-1)
                if j > 0:
                    for c in range(k + 1):
                        if dp_cur[j - 1][c] > INF_NEG:
                            nc = c + cell_cost
                            if nc <= k:
                                ns = dp_cur[j - 1][c] + cell_score
                                if ns > dp_cur[j][nc]:
                                    dp_cur[j][nc] = ns

            # move to next row
            dp_prev = dp_cur
            dp_cur = [[INF_NEG] * (k + 1) for _ in range(n)]

        # dp_prev now holds the last row
        best = max(dp_prev[n - 1])
        return best if best > INF_NEG else -1
