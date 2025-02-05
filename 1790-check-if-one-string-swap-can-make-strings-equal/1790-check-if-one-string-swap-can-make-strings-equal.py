class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        # diffs
        swap = None
        swapped = False
        for a,b in zip(s1, s2):
            if a != b and not swap:
                swap = (a,b)
            elif a != b:
                if a != swap[1] or b != swap[0] or swapped:
                    return False
                swapped = True
        return False if swap and not swapped else True

        