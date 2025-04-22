class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        from math import comb
        MOD = 10**9 + 7

        # Sieve to get smallest prime factors for quick factorization
        spf = list(range(maxValue + 1))
        for i in range(2, int(maxValue**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, maxValue + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Factorize a number into its prime exponent counts
        def factorize(x):
            counts = {}
            while x > 1:
                p = spf[x]
                counts[p] = counts.get(p, 0) + 1
                x //= p
            return counts

        # Precompute factorials and inverses for comb(n + k - 1, k)
        max_k = n + 14
        fact = [1] * (max_k + 1)
        for i in range(1, max_k + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (max_k + 1)
        inv_fact[max_k] = pow(fact[max_k], MOD - 2, MOD)
        for i in range(max_k - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def C(a, b):
            if a < b: return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        # For each number from 1 to maxValue, calculate number of ways
        total = 0
        for num in range(1, maxValue + 1):
            pf = factorize(num)
            ways = 1
            for e in pf.values():
                ways = ways * C(n + e - 1, e) % MOD
            total = (total + ways) % MOD

        return total
