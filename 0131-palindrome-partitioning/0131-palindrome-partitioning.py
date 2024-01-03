class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPali(string):
            extra = (len(string) % 2 == 0) 
            return string[:len(string) // 2] == string[len(string):len(string) // 2-extra:-1]


        def backtrack(i):

            if i == len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if isPali(s[i: j+1]):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        
        backtrack(0)
        return res