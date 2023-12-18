class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L = 0
        T = 0
        R = len(matrix[0]) - 1
        B = len(matrix) - 1
        res = []
        while R >= L and B >= T:
            # Top
            res += matrix[T][L:R+1]
            T += 1
            # Right
            res += [x[R] for x in matrix[T:B+1]]
            R -= 1
            # Bot
            res += matrix[B][L:R+1][::-1]
            B -= 1
            # Left
            res += [x[L] for x in matrix[T:B+1]][::-1]
            L += 1

        return res[: len(matrix[0]) *  len(matrix) ]