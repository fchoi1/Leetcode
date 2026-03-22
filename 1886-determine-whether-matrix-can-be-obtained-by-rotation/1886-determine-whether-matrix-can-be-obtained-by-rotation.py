class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        N = len(mat)
        def rotate(mat):
            new = [[None for _ in range(N)] for _ in range(N)]

            for i, row in enumerate(mat):
                for j, val in enumerate(row):
                    new[j][-i-1] = val
                    
            return new

        def check(mat):
            for r1, r2 in zip(mat, target):
                if r1 != r2:
                    return False
            return True

        for _ in range(4):
            if check(mat):
                return True

            mat = rotate(mat)

        return False
