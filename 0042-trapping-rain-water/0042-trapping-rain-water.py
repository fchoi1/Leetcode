class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left = [0] * N
        right = [0] * N
        left[0],right[-1] = height[0],height[-1]
        for i in range(1,N):
            left[i] = max(left[i-1], height[i])
            right[-i-1] = max(right[N-i], height[N-i])

        water = 0
        for l,r, h in zip(left, right, height):
            if h < l and h < r:
                water += min(l,r) - h

        return water