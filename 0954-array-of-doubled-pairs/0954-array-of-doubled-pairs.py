class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        doubleSet = defaultdict(int)
        arr.sort()
        for n in arr:
            if n/2 in doubleSet:
                doubleSet[n/2] -= 1
                if not doubleSet[n/2]:
                    del doubleSet[n/2]
            elif n*2 in doubleSet:
                doubleSet[n*2] -= 1
                if not doubleSet[n*2]:
                    del doubleSet[n*2]
            else:
                doubleSet[n] += 1
        return  len(doubleSet) == 0