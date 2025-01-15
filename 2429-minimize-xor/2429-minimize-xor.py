class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # XOR
        # 1 0 - 1
        # 0 1 - 1
        # 0 0 - 0
        # 1 1 - 0


        # miniize we want all 1's to the right
        # ex 000111
        # if 100101 => given 4 -> 100111 -> 0000010

        # 01010 -> given 1->  x = 01000 => 00010
        # 01010 -> given 2 -> x = 01010 => 00000
        # 01010 -> given 3 -> x = 01011 => 00001

        # fill left then right

        ones = bin(num2).count('1')
        n1 = bin(num1)[2:]
        s = []

        for b in n1:
            if ones > 0 and b == '1':
                s.append('1')
                ones -= 1
            else:
                s.append('0')
        s = s[::-1]
        i = 0
        N = len(s)
        while ones:
            if i >= N:
                s.append("1")
                print("append", s)
            else:
                if s[i] == '0':
                    s[i] = '1'
                else:
                    ones += 1
                i += 1
            ones -= 1
        return int("".join(s[::-1]), 2)

        # 1100
        