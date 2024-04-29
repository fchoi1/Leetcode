class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr = 0 
        for n in nums:
            curr ^= n
        
        kStr = (bin(k)[2:]).zfill(20)
        currStr = (bin(curr)[2:]).zfill(20)
        return sum(a!=b for a,b in zip(kStr, currStr))
