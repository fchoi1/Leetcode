class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        counts = Counter(digits)

        valid = []

        for i in range(100, 1000, 2):
            curr = Counter(list(str(i)))

            for k,v in curr.items():
                if counts[int(k)] < v:
                    break
            else:
                valid.append(i)
        
        return valid
            