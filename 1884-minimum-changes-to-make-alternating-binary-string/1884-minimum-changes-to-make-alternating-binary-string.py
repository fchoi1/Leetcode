class Solution:
    def minOperations(self, s: str) -> int:
        # grredy
        zCount = 0
        oCount = 0

        for i, char in enumerate(s):

            # 1010
            if (i % 2 == 0 and char == '1') or (i % 2 == 1 and char == '0'):
                zCount += 1
            
            #0
            if (i % 2 == 1 and char == '1') or (i % 2 == 0 and char == '0'):
                oCount += 1
        

        return min(oCount, zCount)
     