class Solution:
    def maximum69Number (self, num: int) -> int:
        new = ''
        switched = False
        for s in str(num):
            if s == '6' and not switched:
                new += '9'
                switched = True
            else:
                new += s
        
        return int(new)