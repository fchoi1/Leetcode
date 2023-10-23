class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numMap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        res = []
        def generate(i, combo):
            if i >= len(digits):  
                res.append(combo) 
                return
            digit = digits[i]

            for char in numMap[int(digit)]:
                combo += char
                generate(i+1, combo)
                combo = combo[:-1] 
        generate(0, "")
        return res