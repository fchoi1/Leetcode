class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        arr = [0] if n % 2 == 1 else []
        
        i = 0
        num = 1
        flip = True
        while len(arr) < n:
            if flip:
                arr.append(num)
            else:
                arr.append(-num)
                num += 1
            flip = not flip
            i += 1
        
        return arr
        
        