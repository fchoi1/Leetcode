class Solution:
    def longestBalanced(self, s: str) -> int:
        # 2 pointer or sliding window

        # should be at the min count * 3


        # abcba
        # abbbabbacccc

        # (0,1) (1,1), (2,1), (3,1), (3,2), (4,2), (5,2) (5,3)

        prefix =    {(0,0):-1} # diff a, diff b, diff c
        single_b =  {(0,0):-1} # diff, count of b
        single_c =  {(0,0):-1} # diff, count of c
        single_a =  {(0,0):-1} # diff, count of a

        maps = [prefix, single_a, single_b, single_c]

        curr =      {'a': 0, 'b': 0, 'c': 0}
        longest =   0

        prev_char = None

        for i,char in enumerate(s):
            
            curr[char] += 1

            diff_ab = curr['a'] - curr['b']
            diff_ac = curr['a'] - curr['c']
            diff_bc = curr['b'] - curr['c']

            keys = [(diff_ab, diff_ac),  (diff_bc, curr['a']),  (diff_ab, curr['c']), (diff_ac, curr['b'])]

            for k, prefix in zip(keys, maps):
                if k not in prefix:
                    prefix[k] = i
                else:
                    longest = max(longest, i - prefix[k])
 
            # repeating case
            if prev_char is not None and prev_char == char:
                same += 1
            else:
                same = 1
                
            longest = max(longest, same)
            prev_char = char
     
        
        return longest

