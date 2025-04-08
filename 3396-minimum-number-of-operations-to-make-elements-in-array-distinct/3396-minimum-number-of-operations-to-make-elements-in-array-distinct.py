class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        dupes = {}
        for k,v in count.items():
            if v > 1:
                dupes[k] = v


        N = len(nums)
        ops = 0
        if len(dupes) == 0:
            return ops
        for i in range(0, N, 3):
            ops += 1
            for idx in range(3):
                if i + idx < N and nums[i + idx] in dupes:
                    dupes[nums[i + idx]] -= 1
                    if dupes[nums[i + idx]] < 2:
                        del dupes[nums[i + idx]]
            if len(dupes) == 0:
                return ops

        return 0