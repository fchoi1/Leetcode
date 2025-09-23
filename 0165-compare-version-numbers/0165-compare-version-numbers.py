class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        idx1 = 0
        idx2 = 0

        while idx1 < len(v1) or idx2 < len(v2):
            
            n1 = 0 if idx1 >= len(v1) else int(v1[idx1])
            n2 = 0 if idx2 >= len(v2) else int(v2[idx2])

            if n1 == n2:
                idx1 += 1
                idx2 += 1
                continue
            
            return 1 if n1 > n2 else -1
        
        return 0
            
        