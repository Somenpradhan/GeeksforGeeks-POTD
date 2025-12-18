# Implement Trie class and complete insert(), search() and isPrefix() function for the following queries :

# Type 1 : (1, word), calls insert(word) function and insert word in the Trie
# Type 2 : (2, word), calls search(word) function and check whether word exists in Trie or not.
# Type 3 : (3, word), calls isPrefix(word) function and check whether word exists as a prefix of any string in Trie or not.
# Examples :

# Input: query[][] = [[1, "abcd"], [1, "abc"], [1, "bcd"], [2, "bc"], [3, "bc"], [2, "abc"]]
# Output: [false, true, true]
# Explanation: string "bc" does not exist in the trie, "bc" exists as prefix of the word "bcd" in the trie, and "abc" also exists in the trie.
# Input: query[][] = [[1, "gfg"], [1, "geeks"], [3, "fg"], [3, "geek"], [2, "for"]]
# Output: [false, true, false]
# Explanation: The string "for" is not present in the trie, "fg" is not a valid prefix, while "geek" is a valid prefix of the word "geeks" in the trie.
# Constraints:
# 1 ≤ query.size() ≤ 104
# 1 ≤ word.size() ≤ 103



class Trie:
    class N:
        def __init__(self): self.c, self.e = [None]*26, 0
    def __init__(self): self.r = self.N()
    def insert(self, w):
        n = self.r
        for ch in w:
            i = ord(ch)-97
            n.c[i] = n.c[i] or self.N()
            n = n.c[i]
        n.e = 1
    def search(self, w):
        n = self.r
        for ch in w:
            i = ord(ch)-97
            if not n.c[i]: return 0
            n = n.c[i]
        return n.e
    def isPrefix(self, w):
        n = self.r
        for ch in w:
            i = ord(ch)-97
            if not n.c[i]: return 0
            n = n.c[i]
        return 1