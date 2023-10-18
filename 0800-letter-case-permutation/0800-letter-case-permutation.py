class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(string, i):
            if i == len(s):
                result.append("".join(string))
                return

            if s[i].isdigit():
                backtrack(string + [s[i]], i+1)
            else:
                backtrack(string + [s[i].upper()], i+1)
                backtrack(string + [s[i].lower()], i+1)

            

        def generate(string, index):
            if len(string) == len(s):
                result.append(string)
                return
            if s[index].isdigit():
                generate(string+s[index], index+1)
            else:
                generate(string+s[index].upper(), index+1)
                generate(string+s[index].lower(), index+1)

        # generate("",0)
        backtrack([],0)
        return result
        