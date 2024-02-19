class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                if abs(i - seen[n]) <= k:
                    return True                    
            seen[n] = i
        return False
            
        