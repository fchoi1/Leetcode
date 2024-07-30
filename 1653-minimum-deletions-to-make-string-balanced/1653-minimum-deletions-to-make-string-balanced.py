class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = a = 0
        a_count = []
        b_count = []
        a_total = s.count("a")
        for c in s:
            b_count.append(b)
            if c == 'b':
                b += 1
            else:
                a += 1
            a_count.append(a_total - a)
        
        min_change = inf
        for left, right in zip(b_count, a_count):
            if left + right < min_change:
                min_change = left + right
        return min_change