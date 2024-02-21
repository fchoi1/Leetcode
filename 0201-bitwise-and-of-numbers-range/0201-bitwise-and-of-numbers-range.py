class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        count = 0
        while left < right:
            left >>= 1
            right >>= 1
            count += 1
        return  left << count
        # l = bin(left)[2:].zfill(31)
        # r = bin(right)[2:].zfill(31)
        # res = 0

        # for i in range(31):
        #     if l[i] != r[i]:
        #         return res
        #     res += int(l[i]) * 2 ** (31-i-1) 
        # return res

       
            
        