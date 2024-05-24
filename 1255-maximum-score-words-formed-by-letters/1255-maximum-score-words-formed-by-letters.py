class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # highest scorign word?
        maxScore = 0
        def checkWord(remain, counts):
            for char, count in counts.items():
                if char not in remain or remain[char] < count:
                    return False
            return True

        def getSubset(index, remain, currScore):
            nonlocal maxScore
            if index == len(words):
                maxScore = max(maxScore, currScore)
                return
            
            for i in range(index, len(words)):
                # check if we can make it
                counts = Counter(words[i])
                if checkWord(remain, counts):
                    newRemain = remain.copy()
                    addScore = 0
                    for char, count in counts.items():
                        newRemain[char] -= count
                        addScore += score[ord(char)-ord('a')] * count
                    getSubset(i + 1, newRemain, currScore + addScore)

        charDict = defaultdict(int)
        for char in letters:
            charDict[char] += 1

        getSubset(0, charDict, 0)
                    
        return maxScore