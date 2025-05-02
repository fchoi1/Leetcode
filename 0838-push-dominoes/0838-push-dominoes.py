class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        left = []
        right = []
        curr_l = curr_r = float('inf')
        # Left pass
        # right pass
        N = len(dominoes)
        for i in range(N):
            r = dominoes[i]
            l = dominoes[N - 1 -i]
            if l == 'L':
                curr_l = 1
            elif l == 'R':
                curr_l = float('inf')
            else:
                if curr_l < float('inf'):
                    curr_l += 1
            left.append(curr_l)

            if r == 'R':
                curr_r = 1
            elif r == 'L':
                curr_r = float('inf')
            else:
                if curr_r < float('inf'):
                    curr_r += 1
            right.append(curr_r)


        s = ''
        for l,r in zip(left[::-1], right):
            if l == r:
                s += '.'
            elif l > r:
                s += 'R'
            else:
                s += 'L'
            
        return s