class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)

        target = sum(skill) // (N//2)

        counts = Counter(skill)
        curr = 0
        # print(counts, target)
        for s in skill:
            diff = target - s
            # print(diff, s, counts)
            if diff not in counts:
                return -1
            counts[diff] -=1
            if not counts[diff]:
                del counts[diff]
            curr +=  diff * s
        return curr // 2
        