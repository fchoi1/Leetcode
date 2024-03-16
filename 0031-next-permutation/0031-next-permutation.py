class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        prev = nums[-1]
        for i, val in enumerate(nums[::-1]):
            if prev > val:
                break
            prev = val
        else:
            nums = nums.reverse()
            return

        # First index to swap
        index = len(nums)-i-1

        # loop again and get next highests to swap within range
        for i in range(len(nums)-1, index, -1):
            if nums[i] > nums[index]:
                break

        # swap indexes
        nums[index], nums[i] = nums[i], nums[index]
        # reverse the sub array (no need to sort since it is already in descending order)
        nums[index + 1:] = nums[index + 1:][::-1]
        return
