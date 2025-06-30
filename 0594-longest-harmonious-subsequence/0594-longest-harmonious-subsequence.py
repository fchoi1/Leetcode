class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)

        res = 0
        for k,v in counts.items():
            if k-1 in counts:
                res = max(res, counts.get(k-1) + v)
            
            if k + 1 in counts:
                res = max(res, counts.get(k+1) + v)
        
        return res