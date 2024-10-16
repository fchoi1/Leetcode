class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # heap?
        curr = sorted([(a,"a"), (b, "b"), (c, "c")], reverse=True)
        string = ""
        prev = None
        while sum(c for c,l in curr) > 0:
            count, letter = curr[0]

            if letter == prev and curr[1][0] <= 0:
                break
            elif letter == prev:
                string += curr[1][1]
                curr[1] = (curr[1][0] - 1, curr[1][1])
                prev = None

            elif count >= 2:
                string += letter * 2
                prev = letter
                curr[0] = (count - 2,letter)
            else:
                string += letter
                prev = None 
                curr[0] = (count - 1,letter)
            curr.sort(reverse=True)
        return string