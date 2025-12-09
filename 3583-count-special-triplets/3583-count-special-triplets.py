class Solution:
    def specialTriplets(self, nums: List[int]) -> int:


        def countBefore(numArr):
            seen = defaultdict(int)
            arr = []
            for n in numArr:
                arr.append(seen[n*2])
                seen[n] += 1
            return arr
        
        front = countBefore(nums)
        back = countBefore(nums[::-1])[::-1]

        mod = 10 ** 9 + 7
        ans = 0
        for f,b in zip(front,back):
            if f == 0 or b == 0:
                continue
            ans += f * b
            ans %= mod

        return ans

