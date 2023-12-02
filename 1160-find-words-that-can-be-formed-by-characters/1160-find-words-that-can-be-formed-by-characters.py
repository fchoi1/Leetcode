class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charList = [0] * 26
        count = 0 
        for char in chars:
            charList[ord(char) - ord('a')] += 1
            
        for word in words:
            wordList = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                wordList[index] += 1
                if wordList[index] > charList[index]:
                    break
            else:
                count += len(word)
        return count
                    
                