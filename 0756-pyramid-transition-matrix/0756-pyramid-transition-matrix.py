class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # backtrack
        # dp?

        allowMap = defaultdict(list)
        allowSet = set(allowed)
        for string in allowed:
            bot =  string[:2]
            top = string[2]
            allowMap[bot].append(top)

        N = len(bottom)

        # bfs

        def checkValid(row, currSet):

            if len(row) == 1:
                return True
            
            nextRows = [('', currSet)] # (nextRow, nextSet)

            # generate all rows?
            for a,b in zip(row, row[1:]):

                bot = a + b

                # invalid row
                if len(allowMap[bot]) == 0:
                    return False
                
                temp = []
                for top in allowMap[bot]:
                    for nextRow, nextSet in nextRows:
                        nextRow += top

                        temp.append((nextRow, nextSet & set(bot)))

                nextRows = temp


            for nextRow, nextSet in nextRows:
                if checkValid(nextRow, nextSet):
                    return True

            return False
                # get possible, construct all combos?


        return checkValid(bottom, set())
