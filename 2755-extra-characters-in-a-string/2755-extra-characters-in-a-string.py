class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        minChar = inf
        wordDict = set(dictionary)
        
        @cache
        def backtrack(word, minChar):
            if not word:
                return minChar
            minC = inf
            for i in range(1,len(word)+1):
                if word[:i] not in wordDict:
                    minC = min(minC,backtrack(word[i:],minChar + i))
                else:
                    minC = min(minC, backtrack(word[i:],minChar))
            return minC
        return backtrack(s, 0)
                

        