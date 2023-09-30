class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentance in sentences:
            maxWords = max(maxWords, len(sentance.split(' ')))
        return maxWords
        