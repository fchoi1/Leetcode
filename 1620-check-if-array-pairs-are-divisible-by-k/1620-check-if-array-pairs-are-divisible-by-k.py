class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        arr_mod = [n % k for n in arr]
        counts = Counter(arr_mod)

        if 0 in counts and counts[0] % 2 != 0:
            return False
        del counts[0]

        for n, c in counts.items():
            diff = k - n
            if c != counts[diff]:
                return False
        return True