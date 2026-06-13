class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        ans = ''
        m = {i:c for i, c in enumerate(string.ascii_lowercase[::-1])}

        for word in words:
            w = 0
            for char in word:
                w += weights[ord(char) - ord('a')]
            ans += m[w % 26]
        return ans