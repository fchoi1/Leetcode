class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
    
        minVal = min(min(basket1),min(basket2))

        c1 = Counter(basket1)
        c2 = Counter(basket2)

        total = c1 + c2

        swaps = [] #val, swaps
        swapCount = 0
        for k,v in total.items():
            if v % 2 == 1:
                return -1
            
            target = v // 2
            if abs(c1[k] - target) != 0:
                swaps.append((k, abs(c1[k] - target)))
                swapCount += abs(c1[k] - target)

        swaps.sort()
        idx = 0
        ans = 0
        swapCount //= 2

        while swapCount > 0:
            val, count = swaps[idx]
            effectiveVal = min(val, minVal * 2)
            use = min(count, swapCount)
            ans += effectiveVal * use
            swapCount -= use
            idx += 1
        return ans
        
