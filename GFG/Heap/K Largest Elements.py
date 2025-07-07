class Solution:
    def kLargest(self, arr, k):
        return sorted(arr, reverse=True)[:k]
# Example usage:
# sol = Solution()
# print(sol.kLargest([3, 2, 1, 5, 6, 4], 2))  # Output: [6, 5]