class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # half?
        if int(n) < 11:
            return str(int(n)-1)

        isEven = len(n) % 2 == 0
        half = n[:(len(n) + int(not isEven)) // 2]
        half_num = int(half)

        #even
        num0 = str(half_num + 1)[:-1] + str(half_num + 1)[:-1][::-1]
        num1 = str(half_num + 1) + str(half_num + 1)[::-1]
        num2 = str(half_num) + str(half_num)[::-1]
        num3 = str(half_num - 1) + str(half_num - 1)[::-1]
        num4 = str(half_num - 1) + "9" + str(half_num - 1)[::-1] 

        # odd       
        num5 = str(half_num + 1) + str(half_num + 1)[:-1][::-1]
        num6 = str(half_num) + str(half_num)[:-1][::-1]
        num7 = str(half_num - 1) + str(half_num - 1)[:-1][::-1]

        diff = inf
        ans = ""
        palis = []
        for numStr in [num0, num1, num2, num3, num4, num5, num6, num7, "9"]:
            print(numStr)
            if numStr.isnumeric():
                palis.append(int(numStr))
        
        for num in sorted(palis):
            if abs(int(n) - num) < diff and num != int(n):
                diff = abs(int(n) - int(num))
                ans = str(num)
        return ans



       