class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        newS = ''
        for i in range(0,len(s), 2*k):
            newS += s[i:i+k][::-1]
            print(newS)
            newS += s[i+k:i+2*k]
        return newS
