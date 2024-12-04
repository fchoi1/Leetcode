class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = j = 0

        def getNext(char):
            if char == 'z':
                return 'a'
            return chr(ord(char) + 1)

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or getNext(str1[i]) == str2[j]:
                j += 1
            i += 1

        return True if j >= len(str2) else False
        