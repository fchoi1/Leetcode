class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        prev = prices[0]
        running = 1
        for p in prices[1:]:
            if prev - p == 1:
                running += 1
            else:
                count += running * (running + 1) / 2
                running = 1
            prev = p
        return int(count +  running * (running + 1) / 2 )
