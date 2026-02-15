class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A, B = len(a), len(b)
        i, j, carry = 0,0,0
        a = a[::-1]
        b = b[::-1]
        ans = ''

        while i < A or j < B:
            n1 = 0 if i >= A else int(a[i])
            n2 = 0 if j >= B else int(b[j])

            total = n1 + n2 + carry
           
            carry = total // 2
            val = total % 2
            print(n1, n2, carry, val)

            ans = str(val) + ans

            i += 1
            j += 1

        if carry:
            ans = str(carry) + ans
        
        return ans