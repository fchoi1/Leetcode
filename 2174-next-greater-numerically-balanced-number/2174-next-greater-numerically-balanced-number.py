class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        

        combos = []
        num_str = str(n)
        N = len(num_str)
        
        # Optimized permutation finding, in ascending order
        def getCombos(i,val,targetLen):

            if len(val) > targetLen:
                return
            elif len(val) == targetLen:
                combos.append(val)
                return 

            
            for idx in range(i, 7):
                if idx + len(val) > targetLen:
                    break
                getCombos(idx + 1, val + str(idx) * idx, targetLen)

        # Generate combos for length N only (sorted)
        getCombos(1, '',N)
        
        minCombos = [1,22,122,1333,14444,122333,1224444]

        valid = inf
        for combo in combos:

            # check if the largest possible permutation is valid first
            if n >= int(combo[::-1]):
                continue

            # calculate perms of length N only
            perms = [''.join(p) for p in permutations(combo)]

            # get min valid 
            for p in perms:
                if int(p) > n:
                    valid = min(valid, int(p))

        # if no valid, get the next highest
        if valid == inf:
            return minCombos[N]
            
        return valid