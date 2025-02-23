class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        def calc(s):
            arr = []
            for prev,curr in zip(s, s[1:]):
                arr.append((prev+ curr)%10)
            return arr
        
        arr = list(map(int, list(s)))
        
        while len(arr) > 2:
            arr = calc(arr)
        
        return arr[0] == arr[1]