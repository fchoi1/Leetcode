class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        binary = bin(n)[2:][::-1]
        print(binary)

        # for i in binary[1::2]:
        #     print(i, i=='1')
        # print([num == '1' for num in binary[1::2]])
        return [sum(num == '1' for num in binary[::2]),sum(num == '1' for num in binary[1::2])  ]