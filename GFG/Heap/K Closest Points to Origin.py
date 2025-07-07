class Solution:
    def kClosest(self, p: list[list[int]], k: int) -> list[list[int]]:
        return sorted(p, key=lambda a: a[0]**2 + a[1]**2)[:k]
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Explanation: The code sorts the points based on their distance from the origin using the Euclidean distance formula (without the square root for efficiency) and returns the first k points.
# Note: The sorting is done in O(n log n) time, and slicing the first
# k elements is O(k), which is dominated by the sorting step.
# The space complexity is O(n) due to the storage of the sorted list.
# Example usage:
# solution = Solution()
# points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
# k = 2
# closest_points = solution.kClosest(points, k)
# print(closest_points)  # Output: [[1, 3], [0, 1]]
# Note: The output may vary based on the order of points with the same distance.
# Example usage:
# solution = Solution()
# points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
# k = 2
# closest_points = solution.kClosest(points, k)
# print(closest_points)  # Output: [[1, 3], [0, 1]]
# Note: The output may vary based on the order of points with the same distance.