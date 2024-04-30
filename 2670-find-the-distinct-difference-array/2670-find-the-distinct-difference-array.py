class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        counts = dict(c)
        seen = set()
        ans = []
        for n in nums:
            counts[n] -= 1
            if counts[n] == 0:
                del counts[n]
            seen.add(n) 
            ans.append(len(seen)-len(counts))
        return ans