class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        d = set() # total sums
        d.add(0)

        for n in nums:
            temp = set(d)
            for i in d:
                if i + n == target:
                    return True
                temp.add(i + n)
            d = temp
        
        return target in d


        