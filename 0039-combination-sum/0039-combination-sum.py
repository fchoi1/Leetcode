class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        seen = set()
        comboList = []
        def countCombos(currSum, currCombo):
            if currSum > target or len(comboList) > 150:
                return

            currCombo.sort()
            key = ",".join(map(str, currCombo))

            if key in seen:
                return
            seen.add(key)

            if currSum == target:
                comboList.append(currCombo)
                return
            
            for n in candidates:
                tempCombo = currCombo[:]
                tempCombo.append(n)
                countCombos(currSum + n,tempCombo)

        countCombos(0,[])
        return comboList