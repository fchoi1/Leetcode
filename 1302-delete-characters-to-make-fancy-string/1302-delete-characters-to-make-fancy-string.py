class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        string = ""
        for i in range(0,len(s)-2):
            if s[i] == s[i+1] and s[i+1] == s[i+2]:
                continue
            string += s[i]
        return string + s[-2] + s[-1]