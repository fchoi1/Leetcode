class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counts = Counter(operations)
        return counts["++X"] + counts["X++"] - counts["X--"] - counts["--X"]