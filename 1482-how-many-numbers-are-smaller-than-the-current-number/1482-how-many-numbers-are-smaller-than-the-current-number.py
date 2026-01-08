class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        N = max(nums) + 1
        c = [0 for _ in range(N)]
        curr = 0
        for i in range(N):
            c[i] = curr
            if i in counts:
                curr += counts[i]

        print(counts, c)
        ans = []
        for n in nums:
            ans.append(c[n])
        
        return ans