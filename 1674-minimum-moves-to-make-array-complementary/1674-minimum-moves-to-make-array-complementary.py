class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # pairs and diff

        N = len(nums)
        sums = [0] * (2 * limit + 2)


        for i in range(N//2):
            minN, maxN = min(nums[i], nums[N-1-i]), max(nums[i], nums[N-1-i])

            sums[2] += 2
            sums[minN + 1] -= 1
            sums[maxN + limit + 1] += 1

            target = maxN + minN

            sums[target] -= 1
            sums[target + 1] += 1

        ans = inf
        curr = 0 
        for val in range(2, 2 * limit + 1):
            curr += sums[val]
            ans = min(ans, curr)
        return ans