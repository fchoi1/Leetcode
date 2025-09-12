class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # we need them to existg in the list

        # a,b,c must be in triplets

        # also need at least 2 of the values to be less than target per triplet

        # 4,4,4
        # 4 2 2
        # 4 5 5  cant
        # 2 2 2 doesnt matter

        found_a = found_b = found_c = False

        for a,b,c in triplets:
            if a == target[0]:
                if b <= target[1] and c <= target[2]:
                    found_a = True
            
            if b == target[1]:
                if a <= target[0] and c <= target[2]:
                    found_b = True
            
            if c == target[2]:
                if a <= target[0] and b <= target[1]:
                    found_c = True
            
            # early return
            if all((found_a, found_b, found_c)):
                return True
        

        return found_a and found_b and found_c
