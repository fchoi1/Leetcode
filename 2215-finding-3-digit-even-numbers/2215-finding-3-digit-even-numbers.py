class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # three digits
        numList = []
        digits.sort()
        seen = set()
        def getPermutations(numStr, digits):
            if numStr in seen:
                return
            seen.add(numStr)
            if len(numStr) == 3:
                num = int(numStr)
                if num >= 100 and num % 2 == 0:
                    numList.append(num)
                return

            for i,n in enumerate(digits):
                temp = digits.copy()
                temp.pop(i)
                getPermutations(numStr + str(n),temp)
        getPermutations('', digits)
        return numList