class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        if k == 0:
            return [0] * N

        code += code
        if k > 0:
            curr = sum(code[1:1+k])
        else:
            curr = sum(code[k:])
        arr = [curr]
        for i in range(1,N):
            if k > 0:
                curr += code[k+i] - code[i]
            else:
                curr += code[i-1] - code[k + i-1]
            i += 1
            arr.append(curr)

        return arr

        
        