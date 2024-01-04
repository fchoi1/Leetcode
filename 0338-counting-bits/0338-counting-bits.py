class Solution:
    def countBits(self, n: int) -> List[int]:
        res =  []
        for i in range(0, n+1):
            count = 0
            while i:
                count += i &  1
                i >>= 1
            res.append(count)
            # res.append(bin(i).count('1'))
        return res
        