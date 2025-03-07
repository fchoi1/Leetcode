class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # binary search
        # get primes between left and right

    # 1200 primes in 10^6

        primes = [True] * (right + 1)
        primes[0] = False
        primes[1] = False
        i = 2
        for i in range(2, int(right ** 0.5) + 1):
            if primes[i]:
                for j in range(2 * i, right + 1, i):
                    primes[j] = False
           

        primeRange = primes[left:right+1]
        minRange = inf
        ans = (-1, -1)  
        prev = None
        
        for i, isPrime in enumerate(primeRange):
            if isPrime:
                if prev and left + i - prev < minRange:
                    minRange = left + i - prev
                    ans = (prev, left + i)
                prev = left + i
      
        return ans

        