class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        trusts = defaultdict(int)
        trusted = set()
        for a,b in trust:
            trusts[b] += 1
            trusted.add(a)
        for person,count in trusts.items():
            if count == n - 1 and person not in trusted:
                return person
        return -1
        