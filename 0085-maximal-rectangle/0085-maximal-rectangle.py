class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # prefix sum
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


            print(stack, row, maxArea, y)
            while stack:
                height, index = stack.pop()
                width = W - index
                print("stack remain", height, width, index)
                maxArea = max(maxArea, height* width)
    
            prev = row

        return maxArea

        