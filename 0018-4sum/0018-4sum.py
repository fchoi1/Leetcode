class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        found = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                find = target - nums[j] - nums[i]
                while left < right:
                    if nums[left] + nums[right] == find:
                        found.add((nums[i], nums[j], nums[left], nums[right]))
                        right -= 1
                    elif nums[left] + nums[right] > find:
                        right -= 1
                    else:
                        left += 1


        return list(found)
        