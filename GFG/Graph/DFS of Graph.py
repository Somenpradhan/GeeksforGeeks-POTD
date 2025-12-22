
# Given a **connected undirected graph** represented by a **2D adjacency list `adj[][]`**, where `adj[i]` represents the list of vertices connected to vertex `i`.  
# Perform a **Depth First Search (DFS) traversal** starting from **vertex 0**, visiting vertices from left to right as per the given adjacency list.

# Return a list containing the **DFS traversal** of the graph.

# **Note:** Traverse nodes in the same order as given in the adjacency list.

# > Note: Sorry for uploading late, my exam is going on.

# ## 🔍 **Example Walkthrough:**

# ### **Example 1:**

# #### **Input:**

# ```
# adj = [[2, 3, 1],
#        [0],
#        [0, 4],
#        [0],
#        [2]]
# ```

# <img src="https://github.com/user-attachments/assets/5ab8ff7f-c58c-4035-9993-4de191cf627b" width="40%">

# #### **Output:**

# ```
# [0, 2, 4, 3, 1]
# ```

# #### **Explanation:**

# The DFS traversal proceeds as follows:

# - **Start at vertex `0`** → Output: `[0]`
# - **Visit `2` (first neighbor of `0`)** → Output: `[0, 2]`
# - **Visit `4` (first neighbor of `2`)** → Output: `[0, 2, 4]`
# - **Backtrack to `2`, then backtrack to `0`, visit `3`** → Output: `[0, 2, 4, 3]`
# - **Backtrack to `0` and visit `1`** → Final Output: `[0, 2, 4, 3, 1]`

# ### **Example 2:**

# #### **Input:**

# ```
# adj = [[1, 2],
#        [0, 2],
#        [0, 1, 3, 4],
#        [2],
#        [2]]
# ```

# <img src="https://github.com/user-attachments/assets/ab16fb62-988e-4cf6-be87-6aacb50fe9c5" width="40%">

# #### **Output:**

# ```
# [0, 1, 2, 3, 4]
# ```

# #### **Explanation:**

# The DFS traversal proceeds as follows:

# - **Start at vertex `0`** → Output: `[0]`
# - **Visit `1` (first neighbor of `0`)** → Output: `[0, 1]`
# - **Visit `2` (first neighbor of `1`)** → Output: `[0, 1, 2]`
# - **Visit `3` (first neighbor of `2`)** → Output: `[0, 1, 2, 3]`
# - **Backtrack to `2` and visit `4`** → Final Output: `[0, 1, 2, 3, 4]`

# ## **Constraints:**

# - $1 \leq$ `adj.size()` $\leq 10^4$
# - $1 \leq$ `adj[i][j]` $\leq 10^4$


class Solution:
    def dfs(self, adj):
        r, v = [], [False] * len(adj)
        def go(i):
            v[i] = True
            r.append(i)
            for j in adj[i]:
                if not v[j]:
                    go(j)
        for i in range(len(adj)):
            if not v[i]:
                go(i)
        return r
