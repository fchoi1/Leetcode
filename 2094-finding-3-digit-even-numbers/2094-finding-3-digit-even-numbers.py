class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digitCount = Counter(digits)
        ans = []
        for n in range(100, 1000, 2):
            check = Counter(str(n))
            for key, counts in check.items():
                if int(key) not in digitCount or counts > digitCount[int(key)]:
                    break
            else:
                ans.append(n)
        return ans


        