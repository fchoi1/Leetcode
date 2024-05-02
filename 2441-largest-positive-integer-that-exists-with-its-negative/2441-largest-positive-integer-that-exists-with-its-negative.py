class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = set()
        pos = set()
        maxNum = 0
        for n in nums:
            if n < 0:
                neg.add(-n)
            else:
                pos.add(n)
            if abs(n) in neg and abs(n) in pos:
                maxNum = max(maxNum, abs(n))
        return maxNum if maxNum else -1

        