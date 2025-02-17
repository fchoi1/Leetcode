class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # bt   
        self.unique = set()

        def backtrack(s, remain):
            if s in self.unique:
                return
            
            self.unique.add(s)
            temp = remain.copy()
            for i,c in temp:
                remain.remove((i,c))
                backtrack(s + c, remain)
                remain.add((i,c))
                
        backtrack("", {(i,c) for i,c in enumerate(tiles) })
        return len(self.unique) - 1
        # for t in tiles:
        #     counts[t] += 1
        #     if not dp:
        #         dp.append(1)
        #     else:
        

        # A A -> 2
        # A A A -> A, AA, AAA
        # A B A -> A , B, AB, BA, AA, BAA, ABA, AAB,
        # A B C -> A, B, C, AB, BA, AC, CA, BC, CB, ABC, ACB, BAC, BCA, CAB, CBA

        # 1 3 11 49

        # A B C D -> A, B, C, AB, BA, AC, CA, BC, CB, ABC, ACB, BAC, BCA, CAB, CBA

        