class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        
        curr = 0
        sign = 1
        i = 0
        while i < k:
            curr += sign
            i += 1
            if curr >= n - 1:
                sign = -1
            if curr == 0:
                sign = 1
        return curr