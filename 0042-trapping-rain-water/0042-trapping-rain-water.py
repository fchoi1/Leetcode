class Solution:
    def trap(self, height: List[int]) -> int:
        # monotonic stacK?
        left = [height[0]]
        right = [height[-1]]
        N = len(height)
        for i in range(1,N):
            left.append(max(left[-1], height[i]))
            right.append(max(right[-1], height[-i]))
        right.reverse()
        # print(left, right)
        water = 0
        for l,r, h in zip(left, right, height):
            if h < l and h < r:
                print(l,h,r)
                water += min(l,r) - h

        return water