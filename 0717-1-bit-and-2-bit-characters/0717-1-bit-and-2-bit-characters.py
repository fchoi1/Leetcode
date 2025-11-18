class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        single = False
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                single = True
            else:
                i += 2
                single = False
                
        return single

      