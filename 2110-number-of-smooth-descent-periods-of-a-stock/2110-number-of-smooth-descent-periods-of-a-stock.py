class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        # while lower, each one is the same
        # 3 -> 6 options
        # 3 2 1 ,  2 1, 1,  3 , 2, 1
        # 3(4 * 1)/2
        count = 0
        prev = prices[0]
        running = 1
        for p in prices:
            if prev - p == 1:
                running += 1
            else:
                count += running * (running + 1) / 2
                running = 1
            prev = p
        if running > 1:
            count += running * (running + 1) / 2 - 1
        return int(count)
