class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 1100
        # 0101
        # 0011
    
        ones = 1 if s[0] == '1' else 0
        zeros = 1 if s[0] == '0' else 0
        pairs = 0

        for prev, curr in zip(s, s[1:]):
            if curr != prev:
                pairs += min(ones, zeros)
                if curr == '1':
                    ones = 0
                else:
                    zeros = 0
            
            if curr == '1':
                ones += 1
            else:
                zeros += 1
            

        pairs += min(ones, zeros)
        return pairs