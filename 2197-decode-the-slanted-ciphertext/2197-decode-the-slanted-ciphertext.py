class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
 
        N = len(encodedText)
        rowLen = N // rows
        ans = ''
        for start in range(rowLen):
            for r in range(rows):
                idx = start + r * rowLen + r
                if idx < N:
                    ans += encodedText[idx]
                else:
                    break
        
        return ans.rstrip()