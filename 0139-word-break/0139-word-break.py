class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set()

        for word in wordDict:
            wordSet.add(word)

        cache = {}
        def checkWord(word):
            if word in cache:
                return cache[word]
                
            if not word:
                return True

            for i in range(len(word)+1, 0, -1):
                if word[:i] in wordSet:
                    cache[word[:i]] = True
                    if checkWord(word[i:]):
                        cache[word] = True
                        return True
            cache[word] = False
            return False

        return checkWord(s)
        