# Given a matrix mat[][], where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
# 0 : Empty cell
# 1 : Cell have fresh oranges
# 2 : Cell have rotten oranges

# Your task is to determine the minimum time required so that all the oranges become rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

# Note: If it is impossible to rot every orange then simply return -1.

# Examples:

# Input: mat[][] = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
# Output: 2
# Explanation: Oranges at positions (0,0), (0,3), (1,3), and (2,3) will rot adjacent fresh oranges in successive time frames.
# All fresh oranges become rotten after 2 units of time.
# Input: mat[][] = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
# Output: -1
# Explanation: Oranges at positions (0,0), (0,3), (1,3), and (2,3) rot some fresh oranges,
# but the fresh orange at (2,0) can never be reached, so not all oranges can rot.
# Constraints:
# 1 ≤ mat.size() ≤ 500
# 1 ≤ mat[0].size() ≤ 500
# mat[i][j] = {0, 1, 2} 


from collections import deque
class Solution:
    def orangesRotting(self, a):
        n, m, f, t = len(a), len(a[0]), 0, 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if a[i][j] == 2:
                    q.append((i, j))
                elif a[i][j] == 1:
                    f += 1
        if not f: return 0
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            sz, ch = len(q), False
            for _ in range(sz):
                i, j = q.popleft()
                for di, dj in d:
                    x, y = i + di, j + dj
                    if x < 0 or y < 0 or x >= n or y >= m or a[x][y] != 1:
                        continue
                    a[x][y] = 2
                    q.append((x, y))
                    f -= 1
                    ch = True
            if ch: t += 1
        return t if f == 0 else -1