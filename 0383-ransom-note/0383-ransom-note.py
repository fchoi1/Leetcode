class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMag = [0] * 26
        for char in magazine:
            charMag[ord(char)- ord('a')] +=1

        for char in ransomNote:
            index = ord(char)- ord('a')
            charMag[index] -=1
            if charMag[index] < 0:
                return False
        return True
        