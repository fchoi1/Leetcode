class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = a = 0
        a_total = s.count("a")
        min_delete = math.inf

        for c in s:
            if c == 'b':
                min_delete = min(min_delete, b + a_total - a)
                b += 1
            else:
                a += 1
                min_delete = min(min_delete, b + a_total - a)
        return min_delete
