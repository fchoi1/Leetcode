class Solution:
    def findScore(self, nums: List[int]) -> int:
        sortedIndex = []
        for i, n in enumerate(nums):
            sortedIndex.append((n,i))

        sortedIndex.sort()

        seen = set()
        score = 0
        for n,i in sortedIndex:
            if i not in seen:
                score += n
                seen.add(i)
                seen.add(i+1)
                seen.add(i-1)

        return score