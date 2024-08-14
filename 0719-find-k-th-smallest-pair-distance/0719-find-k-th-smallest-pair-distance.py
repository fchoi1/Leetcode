class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs(nums, max_dist) -> int:
            count = 0
            N = len(nums)
            left = 0

            for right in range(N):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left
            return count

        nums.sort()
        array_size = len(nums)

        l = 0
        r = nums[array_size - 1] - nums[0]

        while l < r:
            mid = (l + r) // 2

            count = count_pairs(nums, mid)

            if count < k:
                l = mid + 1
            else:
                r = mid

        return l

  