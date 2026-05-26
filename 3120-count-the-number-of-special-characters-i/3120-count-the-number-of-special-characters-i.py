class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        w = set(word)
        
        return sum( x.upper() in word and x in word for x in  list(string.ascii_lowercase))
 