class Solution:
    def reverse(self, x: int) -> int:
        
        newInt =  int(str(abs(x))[::-1])
        if x < 0:
            newInt *= -1
        if newInt < -2*31  or newInt > 2**31-1:
            return 0
        return newInt