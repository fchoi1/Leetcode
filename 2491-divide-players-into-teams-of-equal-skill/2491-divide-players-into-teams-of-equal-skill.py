class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill) // 2
        target = sum(skill) // N
        counts = Counter(skill)
        curr = 0
        for s in skill:
            diff = target - s
            if diff not in counts or counts[diff] == 0:
                return -1
            counts[diff] -= 1
            curr +=  diff * s
        return curr // 2
        