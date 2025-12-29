class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # backtrack
        allowMap = defaultdict(list)
        for string in allowed:
            allowMap[string[:2]].append(string[2])

        def checkValid(row):

            if len(row) == 1:
                return True
            
            nextRows = [''] # (nextRow, nextSet)

            # generate all rows?
            for a,b in zip(row, row[1:]):

                bot = a + b

                # invalid row
                if len(allowMap[bot]) == 0:
                    return False
                
                temp = []
                for top in allowMap[bot]:
                    for nextRow in nextRows:
                        nextRow += top

                        temp.append((nextRow))

                nextRows = temp


            for nextRow in nextRows:
                if checkValid(nextRow):
                    return True

            return False


        return checkValid(bottom)
