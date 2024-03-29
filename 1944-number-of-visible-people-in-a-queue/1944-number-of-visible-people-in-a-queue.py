class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # at each step we want to get the count of tallest values
        # reverse?

        arr = [0]
        prev = heights[-1]
        stack = [prev]
        # heap  to track highest
        for h in heights[:-1][::-1]:
            seen = 0
            if h > prev:
                while stack and h > stack[-1]:
                    stack.pop()
                    seen += 1
                if stack and prev != stack[-1]:
                    seen += 1
        
            stack.append(h)
            arr.append(max(seen, 1))
            prev = h
            
        return arr[::-1]



