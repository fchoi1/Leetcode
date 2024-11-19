class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = curr = i = count = 0
        seen = set()
        N = len(nums)

        for n in nums:
            curr += n
            count += 1
            while n in seen or count > k:
                seen.remove(nums[i])
                curr -= nums[i]
                i += 1
                count -= 1

            if count == k:
                maxSum = max(maxSum, curr)
            seen.add(n)

        return maxSum