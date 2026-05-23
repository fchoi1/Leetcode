class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # prefix sum for quick sum calculation


        # 2d dp problem


        # score (i, k), start at min k

        # choice:
            # create a partition
            # continue with current partition


        # i = index, k = total partitions

        # score(i, 0) for all i = sum(nums) / len(nums)
        # score(i, k) = max( nums[i] + score(i - 1, k-1), nums[i] + nums[i-1] / 2 + score(i - 2, k - 1))

        # avg = (prefix[start] - prefix[end]) / (start - end)

        N = len(nums)
        dp = [0] * (N + 1)

        # preprocess prefix
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [0.0] * (N + 1)

        # base case: 1 group
        for i in range(1, N + 1):
            dp[i] = prefix[i] / i
            
        for _ in range(k - 1):
            temp = [0]
            for i in range(1,N+1):

                best = -inf
                for j in range(i):
                    avg = (prefix[i] - prefix[j]) / (i - j)
                    best = max(best, dp[j] + avg)
                temp.append(best)
            dp = temp

        # prefix[i-1]
        # prefix[i] 

        return dp[-1]

