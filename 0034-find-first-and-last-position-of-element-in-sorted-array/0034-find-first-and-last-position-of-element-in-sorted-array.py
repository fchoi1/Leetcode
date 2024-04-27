class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        # 2 binary searchs?
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        while l < r:
            mid = (l+r)//2

            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        print(l, mid, r)
        low = l if nums[l] == target else l + 1
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        while l < r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        print(l, mid, r)
        high = l if nums[l] == target else l - 1
        if high < 0 or low >= len(nums):
            return [-1,-1]
        return [low, high] if nums[low] == target else [-1,-1]