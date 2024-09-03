class Solution:
    def getLucky(self, s: str, k: int) -> int:
        strNum = ''
        for char in s:
            strNum += str(ord(char) - ord('`'))
        for i in range(k):
            num = 0
            for n in strNum:
                num += int(n)
            strNum = str(num)
        
        return num