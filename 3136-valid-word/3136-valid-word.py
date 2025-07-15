class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3 or not word.isalnum():
            return False

        vowels = "AEIOUaeiou"
        letters = string.ascii_letters
        consonants = set(letters) - set(vowels)
        wordSet = set(word)

        return bool(wordSet & consonants) and bool(wordSet & set(vowels))
