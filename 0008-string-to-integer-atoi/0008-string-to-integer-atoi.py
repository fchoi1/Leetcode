class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        def checkWord(word):
            if not word:
                return 0
            i = 1
            s = word[0]
            while s.isdigit() and i < len(word):
                s += word[i]
                i += 1
            if not s.isdigit() and len(s) == 1:
                return 0
            return int(s) if s.isdigit() else int(s[:-1]) 

        words = s.split(" ")
        for word in words:
            if not word:
                continue
            if word[0] == "+":
                num = checkWord(word[1:])
                return min(2**31-1, num)
            elif word[0] == "-":
                num = checkWord(word[1:])
                return max(-2**31, -num)
            else:
                return min(2**31-1,  checkWord(word))
        return 0
        