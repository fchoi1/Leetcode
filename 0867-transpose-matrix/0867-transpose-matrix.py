class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #3
        return list(zip(*matrix))