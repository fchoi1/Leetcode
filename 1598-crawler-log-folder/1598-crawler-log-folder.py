class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for l in logs:
            if l[:3] == "../":
                level = max(0, level - 1)
            elif l[:2] != "./":
                level += 1
        return level