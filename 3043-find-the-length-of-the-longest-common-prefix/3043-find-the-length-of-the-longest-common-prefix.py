class Trie:
    def __init__(self, val=None, length=0):
        self.val = val
        self.length = length
        self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1 = set(arr1)
        set2 = set(arr2)
        
        root =  Trie()
        for n in set1:
            curr = root
            for i,char in enumerate(str(n)):
                if char not in curr.children:
                    newTrie = Trie(char, i+1)
                    curr.children[char] = newTrie
                curr = curr.children[char]
        
        longest = 0
        for n in set2:
            curr = root
            for c in str(n):
                if c not in curr.children:
                    break
                curr = curr.children[c]
            longest = max(longest, curr.length)
        return longest
                    
                



        