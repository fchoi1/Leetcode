class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        ans = ""
        for char in order:
            ans += char * s_count[char]
            del s_count[char]

        for char, count in s_count.items():
            ans += char * count

        return ans