# Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

# Note: The graph can have multiple component.

# Examples:

# Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
# Output: true
# Explanation: 
 
# 1 -> 2 -> 0 -> 1 is a cycle.
# Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
# Output: false
# Explanation: 
 
# No cycle in the graph.
# Constraints:
# 1 ≤ V, E ≤ 105
# 0 ≤ edges[i][0], edges[i][1] < V


class Solution:
    def isCycle(self, V, edges):
        p = [-1]*V
        def f(x): return x if p[x]<0 else f(p[x])
        for u,v in edges:
            a, b = f(u), f(v)
            if a == b: return True
            if p[a] > p[b]: a,b = b,a
            p[a] += p[b]; p[b] = a
        return False