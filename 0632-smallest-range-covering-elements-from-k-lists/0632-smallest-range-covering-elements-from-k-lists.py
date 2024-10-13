class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        self.r = [-inf, inf]
        nums.sort(key=lambda x: x[0])
        
        def dfs(i, maxVal, minVal):
            if i >= len(nums) or maxVal - minVal > self.r[1] - self.r[0]:
                if maxVal - minVal < self.r[1] - self.r[0]:
                    self.r = [minVal, maxVal]
                return 

            diff_top = diff_bot = inf
            c_top = c_bot = None

            for n in nums[i]:
                if minVal <= n <= maxVal:
                    dfs(i + 1, maxVal, minVal)
                    return

                if n < minVal and minVal - n < diff_bot:
                    diff_bot = minVal - n
                    c_bot = n

                if n > maxVal and n - maxVal < diff_top:
                    diff_top = n - maxVal
                    c_top = n

            if c_bot != None:
                dfs(i + 1, maxVal, min(minVal, c_bot))

            if c_top != None:
                dfs(i + 1, max(maxVal, c_top), minVal)

        curr = [-inf, inf]
        # build ranges
        for n1 in nums[0]:
            dfs(1, n1, n1)
            
        return self.r
 