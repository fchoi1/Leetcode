class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        root = {}

        # build trie from arr1 digits
        for num in arr1:
            curr = root
            for c in str(num):
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]

        longest = 0

        # traverse arr2
        for num in arr2:
            curr = root
            for i, c in enumerate(str(num)):
                if c not in curr:
                    break
                curr = curr[c]
                longest = max(longest, i + 1)

        return longest