# 💡 Problem Description:
# You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of s1.
# Rotation means that the string s2 can be formed by shifting the characters of s1 cyclically.

# Note: The characters in the strings are in lowercase.

# 🔍 Example Walkthrough:
# Input:
# s1 = "abcd", s2 = "cdab"
# Output:
# true

# Explanation:
# After two right rotations, s1 becomes equal to s2.

# Input:
# s1 = "aab", s2 = "aba"
# Output:
# true

# Explanation:
# After one left rotation, s1 becomes equal to s2.

# Input:
# s1 = "abcd", s2 = "acbd"
# Output:
# false

# Explanation:
# The strings are not rotations of each other.

# Constraints:
# (
# 1
# ≤
# s1.size(), s2.size()
# ≤
# 10
# 5
# )


# 🎯 My Approach:
# String Concatenation and Substring Check:

# The solution relies on the fact that a rotated version of s1 will always be a substring of s1 + s1.
# By concatenating s1 with itself, all possible rotations of s1 are included in the resulting string.
# Then, we check if s2 is a substring of the concatenated string.
# Edge Cases:

# If the lengths of s1 and s2 are different, they cannot be rotations.
# Strings with only one character are trivially rotations if they are equal.
# Steps:

# Check if the lengths of s1 and s2 are equal.
# Concatenate s1 with itself to create a new string.
# Use efficient substring search techniques like strstr or KMP to check if s2 is present in the concatenated string.
# 🕒 Time and Auxiliary Space Complexity
# Expected Time Complexity: (O(n)), where (n) is the length of the string. The concatenation takes (O(n)), and the substring search also runs in (O(n)) using algorithms like KMP.
# Expected Auxiliary Space Complexity: (O(n)), as concatenating the string requires additional space for storing (s1 + s1).



# 📝 Solution Code

class Solution:
    def areRotations(self, s1, s2):
        if len(s1) != len(s2):
            return False
        temp = s1 + s1
        return s2 in temp
