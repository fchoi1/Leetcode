class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = None
        for i, n in enumerate(nums):
            if n:
                if prev != None and i - prev <= k:
                    return False
                prev = i
        return True
                
        