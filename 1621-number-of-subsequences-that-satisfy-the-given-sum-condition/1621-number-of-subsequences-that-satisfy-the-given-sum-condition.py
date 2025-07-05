class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # dp
        # does order matter

        nums.sort()

        N = len(nums)

        largest = N - 1
        smallest = 0
        total = 0
        mod = 10**9 + 7

        while smallest <= largest:

            while smallest <= largest and nums[smallest] + nums[largest] > target:
                largest -= 1

            if smallest <= largest and nums[smallest] + nums[largest] <= target:
                total += pow(2, largest - smallest, mod)

            smallest += 1

        return total % mod
