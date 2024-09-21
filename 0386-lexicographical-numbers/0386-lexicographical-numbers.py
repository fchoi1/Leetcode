class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []
        def append_num(arr, start, end):
            for i in range(start,end):
                if n >= i:
                    arr.append(i)
                if n >= i * 10:
                    append_num(arr, i*10, i*10 + 10)
               
        append_num(arr, 1, 10)
        return arr
        
        # 1, 10, 100, 101 .... 11, 110, 111, 112, 113 ... 12,