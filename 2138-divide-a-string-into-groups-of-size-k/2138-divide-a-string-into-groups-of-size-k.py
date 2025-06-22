class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        arr = []
        curr = ""
        for i, char in enumerate(s):
            if i % k == 0 and curr:
                arr.append(curr)
                curr = ""
            curr += char
        
        arr.append(curr.ljust(k, fill))
        return arr