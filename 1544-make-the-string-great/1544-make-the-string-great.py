class Solution:
    def makeGood(self, s: str) -> str:
        # two pointer
        string = []
        for char in s:
            # bad
            if string and char != string[-1] and char.lower() == string[-1].lower():
                string.pop()
                continue
            else:
                string.append(char)
        
        return "".join(string)