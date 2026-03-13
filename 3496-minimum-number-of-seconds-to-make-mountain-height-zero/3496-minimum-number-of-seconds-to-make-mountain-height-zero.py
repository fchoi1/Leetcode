class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        l = 1
        r = mountainHeight * (mountainHeight + 1) // 2 * max(workerTimes)

        while l < r:
            times = (l + r) // 2
            h = 0
            for w in workerTimes:
                h += (-1 + math.sqrt(1 + 8*times/w)) // 2
            
            if h >= mountainHeight:
                r = times
            else:
                l = times + 1
        print(l, r)
        return (l + r) // 2 