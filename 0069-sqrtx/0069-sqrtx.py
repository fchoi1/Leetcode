class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while math.floor(left) < math.floor(right):
            mid = (left + right)/2
            if mid * mid == x:
                return int(mid)
            
            if mid * mid > x :
                right = mid 
            else:
                left = mid

        return  math.floor(right)
            
            
        