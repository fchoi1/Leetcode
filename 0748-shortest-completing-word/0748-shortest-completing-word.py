class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        def isEqual(complete, arr):
            for c1, c2 in zip(complete, arr):
                if c1 != 0 and c1 > c2:
                    return False
            return True

        complete = [0] * 26
        shortest = inf
        shortestWord = ''
        for char in licensePlate:
            if char.isalpha():
                complete[ord(char.lower()) - ord('a')] += 1

        for word in words:
            wordArr = [0] * 26
            for char in word:
                wordArr[ord(char.lower()) - ord('a')] += 1
            if isEqual(complete, wordArr) and len(word) < shortest:
                shortest = len(word)
                shortestWord = word        
        return shortestWord