class Solution:
    def minOperations(self, nums: List[int]) -> int:

        numCount = defaultdict(int)
        for n in nums:
            numCount[n] += 1
        
        minOps = 0
        for count in numCount.values():
            if count == 1:
                return -1
            remain = count % 3 != 0
            minOps += count // 3 + int(remain)
        return minOps
