# Given an array arr[] of non-negative integers of size n. Find the maximum possible XOR between two numbers present in the array.

# Examples:

# Input: arr[] = [25, 10, 2, 8, 5, 3]
# Output: 28
# Explanation: The maximum possible XOR is 5 ^ 25 = 28.
# Input: arr[] = [1, 2, 3, 4, 5, 6, 7]
# Output: 7
# Explanation : The maximum possible XOR is 1 ^ 6 = 7.
# Constraints:
# 2 ≤ arr.size() ≤ 5*104
# 1 ≤ arr[i] ≤ 106


class Solution:
    def maxXor(self, arr):
        max_xor, mask = 0, 0
        for i in range(30, -1, -1):
            mask |= (1 << i)
            prefixes = set()
            temp = max_xor | (1 << i)
            found = False
            for num in arr:
                prefix = num & mask
                if (temp ^ prefix) in prefixes:
                    found = True
                    break
                prefixes.add(prefix)
            if found:
                max_xor = temp
        return max_xor