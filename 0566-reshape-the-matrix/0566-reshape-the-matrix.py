class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        W = len(mat[0])
        H = len(mat)        
        flat = [element for row in mat for element in row ]
        if r * c != len(flat):
            return mat
        res = []
        for i in range(r):
            res.append(flat[i:i+c])
        return res


        