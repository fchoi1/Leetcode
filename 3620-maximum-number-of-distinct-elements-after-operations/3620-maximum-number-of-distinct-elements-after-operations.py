class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # sort?
        nums.sort()
        count = 0
        unique = 1
        maxCount = 2 * k
        print("max", maxCount)
        for prev,curr in zip(nums, nums[1:]):
            # print("prev", prev, "curr", curr, count)

            # track diff
            diff = curr - prev

            if diff == 0:
                if count >= maxCount:
                    continue
                count += 1
            else:
                count -= min(count, diff - 1) 
            unique += 1
        
        return unique

