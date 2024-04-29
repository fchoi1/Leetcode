class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr = 0 
        for n in nums:
            curr ^= n
        
        kStr = (bin(k)[2:]).zfill(20)
        currStr = (bin(curr)[2:]).zfill(20)
        print(curr,kStr,currStr)

        steps = 0
        for a,b in zip(kStr, currStr):
            if a != b:
                steps += 1
        return steps
        # 2 1 3 4

        # 010
        # 001
        #----
        # 011

        # 011
        #----
        # 000
        # 100
        # ---
        # 100
        
        # 001