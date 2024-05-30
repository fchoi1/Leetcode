class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # segments

        #  [    i  j   k   ]
        curr = 0
        seen = {0: (1, 0)} # count, initial
        count = 0
        for i,val in enumerate(arr):
            curr ^= val
            if curr in seen:
                c, total = seen[curr]
                print(i, i * c - total)
                count += i * c - total
                seen[curr] = (c + 1, total + i + 1)
            else:
                seen[curr] = (1, i + 1)
        return count
       

        # preprocess prefix xor

        # []
        # subests?
        # 1 2 3 4 5 
        # - 3 0 4 1

        #   2 3 1 6 7
        # 0 2 1 0 6 1
        # - 2 3 3 7 7 

        # 0 0 0 | 0 0 0
        # 0 1 0 | 0 1 0
        # 0 1 1 | 0 0 1
        # 0 0 1 | 0 0 0
        # 1 1 0 | 1 1 0
        # 1 1 1 | 0 0 1


        #   1 1 1 1 
        # 0 1 0 1 0 
        # 11,
        # 11,
        # 111, 111,11
        # 11
