class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # binary search
        # get primes between left and right

    # 1200 primes in 10^6

        primes = set(range(2, right + 1))

        i = 2
        while i <= int(right ** 0.5):
            for j in range(2 * i, right + 1, i):
                primes.discard(j)
            i += 1
            while i not in primes and i <= int(right ** 0.5):
                i += 1

        primes = list(primes)
        minRange = inf
        ans = (-1, -1)
        for n1, n2 in zip(primes, primes[1:]):
            if n1 < left:
                continue
            if n2 - n1 < minRange:
                ans = (n1, n2)
                minRange = n2 - n1
    
        return ans

        