class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        def countLetters(word):
            charList = [0] * 26
            for char in word:
                charList[ord(char) - ord('a')] += 1
            return charList
        
        def isWordinChars(word, charList):
            wordList = countLetters(word)
            return all(wordList[i] <= charList[i] for i in range(26))
        
        charsList = countLetters(chars)
        return sum(len(word) for word in words if isWordinChars(word,charsList))
                    
                