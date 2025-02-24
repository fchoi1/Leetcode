class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while i < len(bits):
            if bits[i]:
                i += 2
                if i == len(bits):
                    return False
            else:
                i += 1
        return i == len(bits)
        # return True