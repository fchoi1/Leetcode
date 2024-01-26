class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        strNum = s[1:-1]

        def getValidCount(strFloat, seen):
            result = []

            if float(strFloat) not in seen and (len(strFloat) == 1 or strFloat[0] != '0'):
                seen.add(float(strFloat))
                result.append(strFloat)

            for i in range(1, len(strFloat)):
                left = strFloat[:i]
                right = strFloat[i:]

                # check trailing zeros
                if len(left) > 1 and left[0] == '0' or right[-1] == '0' :
                    return result

                if float(left+"."+right) not in seen:
                    seen.add(float(left+"."+right))
                    result.append(left+"."+right)

            return result


        leftSeen = set()
        rightSeen = set()
        result = []
        for i in range(1, len(strNum)):
            left = strNum[:i]
            right = strNum[i:]
            leftCombo = getValidCount(left, leftSeen)
            rightCombo = getValidCount(right, rightSeen)
            for l in leftCombo:
                for r in rightCombo:
                    result.append(f"({l}, {r})")
        return result
            
 