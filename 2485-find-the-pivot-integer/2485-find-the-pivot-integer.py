class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n,-1, -1):
            left =(n * (n + 1) / 2 ) - (i * (i + 1) / 2)
            right = (i-1) * i / 2
            if left == right:
                return i
            if left > right:
                return -1


        