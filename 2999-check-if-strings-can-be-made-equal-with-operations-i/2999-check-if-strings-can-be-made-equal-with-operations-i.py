class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        
        for i in range(4):
            print(s1, s2)

            if s1[i] == s2[i]:
                continue
            else:
                if i >= 2:
                    return False
                if s1[i + 2] == s2[i]:
                    s1[i+2], s1[i] =  s1[i], s1[i+2]
                elif s2[i + 2] == s1[i]:
                    s2[i+2], s2[i] =  s2[i], s2[i+2]
                else:
                    return False

        return True