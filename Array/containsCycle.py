from typing import List
from collections import deque

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    # BFS starting from (i, j)
                    q = deque()
                    q.append((i, j, -1, -1))   # (x, y, parent_x, parent_y)
                    visited[i][j] = True

                    while q:
                        x, y, px, py = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y]:
                                # Skip the cell we came from
                                if (nx, ny) == (px, py):
                                    continue
                                # If already visited, a cycle is found
                                if visited[nx][ny]:
                                    return True
                                visited[nx][ny] = True
                                q.append((nx, ny, x, y))

        return False
