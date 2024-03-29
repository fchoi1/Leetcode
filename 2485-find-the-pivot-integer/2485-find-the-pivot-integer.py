class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        l, r = 0, n
        
        while l < r:
            i = (l + r) // 2
            right = (n * (n + 1) - i * (i + 1))/2
            left = (i-1) * i / 2
            if left == right:
                return i
            if left > right:
                r = i - 1
            else:
                l = i + 1
        return -1

        