class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # top
        # right 
        # bottom 
        # left
        H = len(matrix)
        W = len(matrix[0])
 
        res = []

        h_loops = (H + 1) // 2
        w_loops = (W + 1) // 2
        odd = H % 2 == 1
        
        print(h_loops, w_loops)
        for l in range(max(h_loops, w_loops)):

            if l < h_loops:
                # top
                for x in range(l, W - l):
                    res.append(matrix[l][x])
            
            print(res, "top",1 + l, H - l)
            if l < w_loops:
                # right
                for y in range(1 + l, H - l):
                    res.append(matrix[y][-l-1])

            print(res, "right",W - 2 - l,  l -1 )
            if l < H - l - 1:
                # bot
                for x in range(W - 2 - l,  l - 1, -1):
                    res.append(matrix[H - 1 - l][x])

            print(res, "bot",H - 2 - l, l)
            if l < W - l - 1:
                # left
                for y in range(H - 2 - l, l, -1):
                    res.append(matrix[y][l])

        # one more pass 
        # print("odd")
        # if odd:
        #     for x in range(loops, W - loops):
        #         res.append(matrix[loops][x])


        return res