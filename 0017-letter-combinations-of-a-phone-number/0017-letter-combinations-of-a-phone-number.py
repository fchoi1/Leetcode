class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numMap = [ "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = []
        def generate(digits, string):
            if len(digits) == 0:
                result.append(string)
                return
            n = int(digits[0]) - 2
            for c in numMap[n]:
                generate(digits[1:], string + c)
        generate(digits,"")
        return result
            