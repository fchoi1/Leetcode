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
        single_a =  {(0,0):-1}

        curr =      {'a': 0, 'b': 0, 'c': 0}
        longest = 1

        prev_char = None

        for i,char in enumerate(s):
            
            curr[char] += 1

            diff_ab = curr['a'] - curr['b']
            diff_ac = curr['a'] - curr['c']
            diff_bc = curr['b'] - curr['c']

            key = (diff_ab, diff_ac)
            key_b = (diff_ab, curr['c'])
            key_c = (diff_ac, curr['b'])
            key_a = (diff_bc, curr['a'])

            if key_a in single_a:
                longest = max(longest, i - single_a[key_a])
            else:
                single_a[key_a] = i

            if key_b in single_b:
                longest = max(longest, i - single_b[key_b])
            else:
                single_b[key_b] = i

            if key_c in single_c:
                longest = max(longest, i - single_c[key_c])
            else:
                single_c[key_c] = i

            if key not in prefix:
                prefix[key] = i
            else:
                longest = max(longest, i - prefix[key])

            if prev_char is not None and prev_char == char:
                same += 1
                longest = max(longest, same)
            else:
                same = 1
                
            prev_char = char
     
        
        return longest

