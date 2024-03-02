class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)
        count = 0
        for i, word1 in enumerate(words[:-1]):
            for word2 in words[i+1:]:
                if isPrefixAndSuffix(word1, word2):
                    count += 1
        return count