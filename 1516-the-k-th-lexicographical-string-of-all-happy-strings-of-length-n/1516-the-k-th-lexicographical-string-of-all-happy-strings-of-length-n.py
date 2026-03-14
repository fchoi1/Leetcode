class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        

        total = 3 * 2 ** (n-1)
        
        if k > total:
            return ''

        if k <= total // 3:
            curr = 'a'
            l = 0
            r = total // 3
        elif total // 3 < k <= total // 3 * 2:
            curr = 'b'
            l = total // 3 + 1
            r = total // 3 * 2
        else:
            curr = 'c'
            l = total // 3 * 2 + 1
            r = total

        mapping = {
            'a': ('b','c'),
            'b': ('a','c'),
            'c': ('a','b')
        }

        string = [curr]
        for _ in range(n-1):
            mid = (l + r) // 2
            if k <= mid:
                curr = mapping[curr][0]
                r = mid
            else:
                curr = mapping[curr][1]
                l = mid
            string.append(curr)

        return "".join(string)

        