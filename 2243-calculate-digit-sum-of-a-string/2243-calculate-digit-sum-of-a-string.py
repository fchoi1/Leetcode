class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            new_s = ''
            length = len(s) // k
            curr = 0
            for i in range(len(s)):
                curr += int(s[i])
                if i != 0 and (i+1) % k == 0:
                    new_s += str(curr)
                    curr = 0
            if len(s) % k != 0:
                new_s += str(curr)

            s = new_s
        
        return s
        
        