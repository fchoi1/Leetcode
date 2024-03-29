class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        prev = nums[0]
        counts = 1
        for n in nums[1:]:
            if n == prev:
                counts += 1
            else:
                counts = 1

            if counts < 3:
                nums[slow] = n
                slow += 1                
            prev = n
        return slow