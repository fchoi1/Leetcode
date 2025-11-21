class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # how many 3 letter palis are there?
        # 26 * 26

        def getCounts(char):
            found = False
            unique = set()
            count = 0

            for i in range(len(s)):
                if s[i] == char:
                    if not found:
                        found = True
                        continue
                    count = len(unique)

                if found:
                    unique.add(s[i])

            return count

        # check unique letters between first and last occurence of a letter
        ans = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            ans += getCounts(c)  

        return ans