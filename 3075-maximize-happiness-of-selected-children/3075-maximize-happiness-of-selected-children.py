class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = i = 0
        while i < k and happiness[i] - i > 0:
            total += happiness[i] - i
            i += 1
        return total
