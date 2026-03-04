class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = []
        count = 0
        for i, row in enumerate(mat):
            if sum(row) == 1:
                for j in range(len(mat[0])):
                    if mat[i][j] == 1 and sum(x[j] for x in mat) == 1:
                        count += 1

        return count
        