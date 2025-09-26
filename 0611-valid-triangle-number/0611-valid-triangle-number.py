class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        # longest < s_1 + s_2
        count = 0
        nums.sort(reverse=True)
        N = len(nums)

        for i, longest in enumerate(nums[:-2]):
            s2 = i + 1
            s1 = N - 1
            target = longest - nums[s2]

            valid = 0
            while s2 < s1:
                if nums[s1] > target:
                    count += (s1 - s2)
                    s2 += 1
                    target = longest - nums[s2]
                else:
                    s1 -= 1
    
        return count
