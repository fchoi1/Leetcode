class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = version1.split('.')
        v2 = version2.split('.')
        p1 = p2 = 0
        while p1 < len(v1) or p2 < len(v2):
            if p1 == len(v1):
                val1 = 0
            else:
                val1 = int(v1[p1])
                p1 += 1
            if p2 == len(v2):
                val2 = 0
            else:
                val2 = int(v2[p2])
                p2 += 1
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
        return 0
        