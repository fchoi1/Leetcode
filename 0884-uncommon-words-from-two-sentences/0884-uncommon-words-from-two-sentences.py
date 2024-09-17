class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count_1 = Counter(s1.split(" "))
        count_2 = Counter(s2.split(" "))

        set_1 = {a for a, c in count_1.items() if c == 1}
        set_2 = {a for a, c in count_2.items() if c == 1}
        return (set_1 - set(count_2)).union(set_2 - set(count_1))
        