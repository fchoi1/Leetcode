class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def generate(string, i):
            if len(string) == len(s):
                return result.append(string)
                
            if s[i].isdigit():
                generate(string+s[i], i+1)
            else:
                generate(string+s[i].upper(), i+1)
                generate(string+s[i].lower(), i+1)
        generate("",0)
        return result
        