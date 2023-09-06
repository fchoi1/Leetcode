class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missing = {}
        
        for i in range(len(nums)):
            if ( (target - nums[i]) not in missing):
                missing[nums[i]] = i
            else:
                return [missing[target - nums[i]], i]
            
        return []
        