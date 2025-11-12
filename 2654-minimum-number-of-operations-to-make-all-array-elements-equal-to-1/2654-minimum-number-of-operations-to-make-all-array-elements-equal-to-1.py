class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        N = len(nums)

        if ones > 0:
            return N - ones

        def get_factors(n):
            factors = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    factors.add(i)
                    factors.add(n // i)
            return factors

        factors = None

        for n in nums:
            if factors == None:
                factors = get_factors(n)
            else:
                factors &= get_factors(n)
            print(n, get_factors(n))

        if len(factors) > 1:
            return -1

        def is_prime(n):
            if n <= 1:
                return False 
            
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False 
            
            return True 

        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        

        # look for prime gcd if possible which should have it
        ans = 0
        while True:
            print("start", nums)
            for i in range(N - 1):
                prev = nums[i]
                curr = nums[i + 1]

                gcd = get_gcd(prev, curr)
                if prev == curr:
                    continue
   
                if gcd == 1:
                    return N + ans
                else:
                    nums[i] = gcd

            ans += 1

        print("huh")
        return N + ans
                

            