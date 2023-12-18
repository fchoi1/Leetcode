class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordSet = defaultdict(int)
        pairs = 0
        for word in words:
            if word[::-1] in wordSet:
                pairs += 2
                wordSet[word[::-1]] -=1
                if wordSet[word[::-1]] == 0:
                    del wordSet[word[::-1]]
            else:
                wordSet[word]+=1
        for word in wordSet:
            if word[0] == word[1]:
                pairs += 1
                break
        return pairs * 2
        