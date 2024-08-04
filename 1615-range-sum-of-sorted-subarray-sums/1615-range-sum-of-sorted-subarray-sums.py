class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10 ** 9 + 7
        total = []
        # n.sort()
        highest = sum(nums)
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                total.append(curr)
        total.sort()
            

        total_sum = 0

        for val in total[left-1:right]:
            total_sum = (total_sum + val) % mod
        return total_sum
