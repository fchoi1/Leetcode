class Trie:
    def __init__(self, val = None, isEnd = False):
        self.next = {} # char: Trie
        self.val = val
        self.end = isEnd

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # trie

        root = Trie()

        for val in arr1:
            curr = root
            for char in str(val):
                if char not in curr.next:
                    curr.next[char] = Trie(char)
                curr = curr.next[char]
        
        longest = 0
        for val in arr2:
            curr = root
            for i, char in enumerate(str(val)):
                if char not in curr.next:
                    break
                curr = curr.next[char]
                longest = max(longest, i + 1)

        return longest