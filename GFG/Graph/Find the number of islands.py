# Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

# Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

# Examples:

# Input: grid[][] = [['L', 'L', 'W', 'W', 'W'], 
#                 ['W', 'L', 'W', 'W', 'L'], 
#                 ['L', 'W', 'W', 'L', 'L'], 
#                 ['W', 'W', 'W', 'W', 'W'], 
#                 ['L', 'W', 'L', 'L', 'W']]
# Output: 4
# Explanation:
# The image below shows all the 4 islands in the grid.
 
# Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'], 
#                 ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
# Output: 2
# Expanation:
# The image below shows 2 islands in the grid.
 
# Constraints:
# 1 ≤ n, m ≤ 500
# grid[i][j] = {'L', 'W'}


class Solution:
    def numIslands(self, g):
        n, m, ans = len(g), len(g[0]), 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or g[i][j]=='W': return
            g[i][j] = 'W'
            for a in (-1,0,1):
                for b in (-1,0,1):
                    dfs(i+a, j+b)
        for i in range(n):
            for j in range(m):
                if g[i][j]=='L':
                    ans += 1
                    dfs(i, j)
        return ans