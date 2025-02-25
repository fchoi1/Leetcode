class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7
        even = 1
        curr = count = odd = 0
        for n in arr:
            curr = (curr + n) % 2

            if curr:
                odd += 1
                count += even % mod
            else:
                even += 1
                count += odd % mod

                
            print(n, "even",even, "odd", odd, "count", count)

            
        return count % mod

        