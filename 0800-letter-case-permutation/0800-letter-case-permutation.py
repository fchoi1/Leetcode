class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        N = len(s)
        def generate(string, index):
            if len(string) == N:
                result.append(string)
                return
            if s[index].isdigit():
                generate(string+s[index], index+1)
            else:
                generate(string+s[index].upper(), index+1)
                generate(string+s[index].lower(), index+1)
        
        generate("",0)
        return result
        