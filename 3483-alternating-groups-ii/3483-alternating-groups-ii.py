class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        # L 4,  K = 3,  3
        # L 5   K = 3,  4

        alt = 1
        groups = 0

        i = 0
        startAlt = 1
        # start
        while i < len(colors):
            if i + 1 < len(colors) and colors[i] != colors[i+1]:
                startAlt += 1
            else:
                break
            i += 1
        print("start",i, startAlt)

        if i >= len(colors) - 1:
            print(startAlt, k, "bnreak")
            return startAlt - k + 1 if colors[0] == colors[-1] else i + 1

        alt = 0
        while i + 1 < len(colors):
            if i + 1 < len(colors) and colors[i] != colors[i + 1]:
                alt += 1
            else:
                groups += max(0, alt - k + 1)
                alt = 1
            i += 1
        
        print("end",i, alt, groups)
        if colors[0] != colors[-1]:
            groups += max(0, alt + startAlt - k + 1)
        else:
            groups += max(0, alt - k + 1)
            groups += max(0, startAlt - k + 1)

        
        return groups
        