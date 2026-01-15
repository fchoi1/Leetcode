class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        N = len(heights)
        ans = [0 for _ in range(N)]
        stack = [] # height, index        

        for i, h in enumerate(heights):
            while stack and h > stack[-1][0]:
                _, idx = stack.pop()
                ans[idx] += 1
                if stack:
                    ans[stack[-1][1]] += 1
                
            stack.append((h,i))
            
        for _, idx in stack[:-1]:
            ans[idx] += 1

        return ans