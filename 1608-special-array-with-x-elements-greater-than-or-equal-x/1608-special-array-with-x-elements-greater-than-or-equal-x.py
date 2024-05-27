class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counts = Counter(nums)
        currCount = prev = 0
        for key, count in sorted(counts.items()):
            # print(key,prev, count,"curr",len(nums)-currCount, currCount)
            if len(nums)-currCount <= key and len(nums)-currCount > prev:
                return len(nums)-currCount
            prev = key
            currCount += count
        return -1