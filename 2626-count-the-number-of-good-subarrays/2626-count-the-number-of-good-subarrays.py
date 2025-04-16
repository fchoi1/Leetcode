class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # 2 pointers

        # once if pass threshold we just count sub arrays

        l = 0
        pairs = 0
        counts = defaultdict(int)
        subArr = 0
        N = len(nums)
    
        for r, n in enumerate(nums):
            counts[n] += 1
            if counts[n] >= 2:
                pairs += counts[n] - 1
            # print(pairs, counts, pairs >= k and l < r, "loop", r, n)
            while pairs >= k and l < r:
                subArr += N - r

                if counts[nums[l]] >= 2:
                    pairs -= counts[nums[l]] - 1
                counts[nums[l]] -= 1
                l += 1

        return subArr
