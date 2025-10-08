class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        M = len(potions)

        # sort
        potions.sort()

        ans = []


        for s in spells:
            target =  math.ceil(success / s)
            idx = bisect.bisect_left(potions, target)
            ans.append(M - idx) 

        return ans