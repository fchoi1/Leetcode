class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        def sieve_of_eratosthenes(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
            
            p = 2
            while (p * p <= limit):
                if is_prime[p]:
                    # Mark all multiples of p as False
                    for i in range(p * p, limit + 1, p):
                        is_prime[i] = False
                p += 1
            
            # Collecting all prime numbers
            return is_prime


        primes = sieve_of_eratosthenes(1000)
        if primes[n]:
            return n 

        dp = [0,1]        
        for i in range(2,n+1):
            if primes[i]:
                dp.append(i)
            else:
                for j in range(2,i):
                    if i % j == 0:
                        dp.append(min(dp[j] + i//j, dp[i//j] + j))
                        break
        return dp[-1]
                


