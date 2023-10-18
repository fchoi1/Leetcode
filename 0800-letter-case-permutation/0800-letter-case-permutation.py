class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(i, path):
            if i == len(s):
                ans.append("".join(path))
                return 

            path.append(s[i].lower())
            backtrack(i + 1, path)
            path.pop()

            if s[i].isalpha():
                path.append(s[i].upper())
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

        return ans
        