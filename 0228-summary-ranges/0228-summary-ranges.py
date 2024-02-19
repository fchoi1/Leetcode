class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start = prev = nums[0]
        for n in nums[1:]:
            if n == prev + 1:
                prev = n
                continue
            val = str(start) if start == prev else f'{start}->{prev}'
            res.append(val)
            start = prev =  n
        res.append(str(start) if start == prev else f'{start}->{prev}')
        return res
                
        