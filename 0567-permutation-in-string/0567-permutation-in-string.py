class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        N = len(s1)
        s1_count = Counter(s1)
        s2_count = Counter(s2[:N])

        if s1_count == s2_count:
            return True

        for i in range(N, len(s2)):
            s2_count[s2[i-N]] -=1
            s2_count[s2[i]] += 1
            if s1_count == s2_count:
                return True
        return False
            
        
        