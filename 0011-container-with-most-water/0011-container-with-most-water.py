class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxWater = 0

        while l < r:
            hl = height[l]
            hr = height[r]

            water = (r - l) * min(hl, hr)
            if hl > hr:
                r -= 1
            else:
                l += 1
            maxWater = max(maxWater, water)


        return maxWater
        