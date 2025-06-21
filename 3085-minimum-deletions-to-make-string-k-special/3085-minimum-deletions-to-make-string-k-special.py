class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word)
        minDelete = inf

        freq = Counter(counts.values())
        sorted_freq = sorted(freq.items())
        for target, _ in sorted_freq:
            delete_top = 0
            delete_bot = 0
            for key, v in sorted_freq:
                if key - target > k:
                    delete_top += v * abs(target - key + k)

                elif target > key:
                    delete_bot += v * key
            minDelete = min(minDelete, delete_top +delete_bot)


        return minDelete
    