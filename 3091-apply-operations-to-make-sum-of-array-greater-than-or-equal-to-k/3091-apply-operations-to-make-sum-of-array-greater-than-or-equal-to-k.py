class Solution:
    def minOperations(self, k: int) -> int:  
        add = int(math.sqrt(k))
        times = k // add if k % add == 0 else k // add + 1
        return add + times - 2
            