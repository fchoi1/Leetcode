class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        val = math.log(n)/math.log(4) 
        return val == int(val)