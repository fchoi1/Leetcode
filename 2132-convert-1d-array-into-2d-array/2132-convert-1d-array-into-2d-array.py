class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []
        return [original[i * n : (i + 1) * n] for i in range(len(original)//n)]
        