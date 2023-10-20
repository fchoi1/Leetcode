class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charNote = [0] * 26
        charMag = [0] * 26
        for char in magazine:
            charMag[ord(char)- ord('a')] +=1

        for char in ransomNote:
            index = ord(char)- ord('a')
            charNote[index] +=1
            if charNote[index] > charMag[index]:
                return False
        return True
        