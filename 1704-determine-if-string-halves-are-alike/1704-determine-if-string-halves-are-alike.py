class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        vCount = vCount2  = 0
        half = len(s)//2
        for i,char in enumerate(s):
            if char in vowels:
                if i < half:
                    vCount += 1
                else:
                     vCount2 += 1
        return vCount == vCount2
        


        