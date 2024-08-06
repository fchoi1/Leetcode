class Solution:
    def minimumPushes(self, word: str) -> int:

        counts = Counter(word)
        sorted_counts = sorted(counts.values(), reverse=True) 
        pushes = 0
        buttons = 0
        for c in sorted_counts:
            pushes += c * (buttons // 8 + 1)
            buttons += 1

        return pushes
        