class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        W = len(matrix[0])
        H = len(matrix)
        prev = []
        maxArea = 0
        for y in range(H):
            row = []
            stack = []
            for x in range(W):
                val = int(matrix[y][x])
                if prev and val == 1:
                    val += prev[x]

                # stack logic max Area
                if stack and val < stack[-1][0]:
                    while stack and val < stack[-1][0]:
                        height, index = stack.pop()
                        width = x - index
                        maxArea = max(maxArea, height* width)
                    stack.append((val, index))
                else:
                    i = x
                    stack.append((val, i))
                row.append(val)

            # Empty Stack afterwards
            while stack:
                height, index = stack.pop()
                width = W - index
                maxArea = max(maxArea, height* width)
            
            # set prev row
            prev = row

        return maxArea

        