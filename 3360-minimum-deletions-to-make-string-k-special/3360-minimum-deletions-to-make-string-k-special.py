class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word)
        minDelete = inf
        freq = Counter(counts.values())
        sorted_freq = sorted(freq.items())
        for target, _ in sorted_freq:
            delete = 0
            for key, v in sorted_freq:

                if key - target > k:
                    delete += v * abs(target - key + k)
                elif target > key:
                    delete += v * key

            minDelete = min(minDelete, delete)

        return minDelete
    