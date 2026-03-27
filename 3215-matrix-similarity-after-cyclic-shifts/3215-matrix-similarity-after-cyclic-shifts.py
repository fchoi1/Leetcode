class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        N = len(mat[0])
        return all( (row + row)[k%N:k%N+N] == row for row in mat)