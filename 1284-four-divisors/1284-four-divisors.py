class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # factors

        def getSumFactors(num):
            N = int(math.sqrt(num)) + 1
            count = 0
            sumCount = 0
            for i in range(1, N):
                if num % i == 0 and n / i != i:
                    count += 2
                    sumCount += num // i
                    sumCount += i
                elif num / i == i:
                    count += 1
                    sumCount += i
            
            if count == 4:
                return sumCount
            return 0

        ans = 0
        for n in nums:
            ans += getSumFactors(n)
        return ans