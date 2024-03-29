class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        arr = [0]
        prev = heights[-1]
        stack = [prev]
        for h in heights[:-1][::-1]:
            seen = 0
            if h > prev:
                while stack and h > stack[-1]:
                    stack.pop()
                    seen += 1
                if stack:
                    seen += 1
            stack.append(h)
            arr.append(max(seen, 1))
            prev = h
            
        return arr[::-1]



