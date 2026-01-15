class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        # forwards then backwards pass

        # start from lower - increasing

        N = len(heights)
        ans = [0 for _ in range(N)]
        stack = [] # height, index        

        for i, h in enumerate(heights):
            currPop = 0
            print("\n")
            while stack and h > stack[-1][0]:
                _, idx = stack.pop()
                print('pop', idx, currPop)
                currPop += 1
                ans[idx] += 1
                if stack:
                    ans[stack[-1][1]] += 1
                
            stack.append((h,i))
            
        for i, (_, idx) in enumerate(stack[:-1]):
            ans[idx] += 1

        print("end", stack)
        print(ans)


        return ans