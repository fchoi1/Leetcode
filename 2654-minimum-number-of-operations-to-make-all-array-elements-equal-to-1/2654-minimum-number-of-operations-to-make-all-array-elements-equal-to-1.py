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

        curr_gcd = nums[0]
        for n in nums:
            curr_gcd = math.gcd(curr_gcd, n)
        if curr_gcd > 1:
            return -1
       

        ans = 0
        while True:
            for i in range(N - 1):
                prev = nums[i]
                curr = nums[i + 1]

                gcd = math.gcd(prev, curr)
                if prev == curr:
                    continue
   
                if gcd == 1:
                    return N + ans
                else:
                    nums[i] = gcd

            ans += 1

        print("ERROR")
        return -1
                

            