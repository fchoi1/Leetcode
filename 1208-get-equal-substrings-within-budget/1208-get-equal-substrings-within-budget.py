class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # cal min cost

        # looks for similar chars

        # slding window

        currCost = slow = longest = 0
        for i in range(len(s)):
            cost = abs(ord(t[i]) - ord(s[i]))
            currCost += cost
            longest = max(longest, i - slow)
            while currCost > maxCost:
                print("sub", abs(ord(t[slow]) - ord(s[slow])))
                currCost -= abs(ord(t[slow]) - ord(s[slow]))
                slow += 1
        return max(longest, i+1 - slow)