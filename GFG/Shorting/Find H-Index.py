# Problem Description:

# You are given an array of integers citations[], where citations[i] is the number of citations a researcher received for the i-th paper. Your task is to find the H-Index of the researcher.

# H-Index is the largest value H such that the researcher has at least H papers that have been cited at least H times.

# 🔍 Example Walkthrough:
# Input:
# citations[] = [3, 0, 5, 3, 0]
# Output:
# 3

# Explanation:
# There are at least 3 papers (with 3, 5, and 3 citations) that have been cited at least 3 times.

# Input:
# citations[] = [5, 1, 2, 4, 1]
# Output:
# 2

# Explanation:
# There are at least 2 papers (with 5 and 4 citations) that have been cited at least 2 times.

# Input:
# citations[] = [0, 0]
# Output:
# 0

# Explanation:
# No paper has been cited at least once.

# Constraints:
# 1
# ≤
# c
# i
# t
# a
# t
# i
# o
# n
# s
# .
# s
# i
# z
# e
# (
# )
# ≤
# 10
# 6
# 0
# ≤
# c
# i
# t
# a
# t
# i
# o
# n
# s
# [
# i
# ]
# ≤
# 10
# 6


# 🎯 My Approach:
# Bucket Sort Method:

# We create an array buckets[] where buckets[i] stores the count of papers with exactly i citations.
# If a paper has citations greater than or equal to the number of papers, it is counted in a special buckets[n].
# After building the bucket, we compute the cumulative count of papers with at least i citations to determine the H-Index.
# Steps:

# Traverse the citations[] array to populate the buckets[].
# Traverse the buckets[] array from the back to compute the cumulative counts and find the H-Index.
# This approach ensures a linear time complexity.
# 🕒 Time and Auxiliary Space Complexity
# Expected Time Complexity: O(n), where n is the size of the citations array. We perform one traversal to populate the buckets[] and another traversal to compute the H-Index.
# Expected Auxiliary Space Complexity: O(n), as we use an array of size n+1 for the bucket sort.



class Solution:
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        cumulative = 0
        for i in range(n, -1, -1):
            cumulative += buckets[i]
            if cumulative >= i:
                return i
        return 0