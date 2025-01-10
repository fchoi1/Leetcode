class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        w1 = []
        w2 = []

        uni = None


        for word in words2:
            temp = [0] * 26
            for s in word:
                temp[ord(s) - ord('a')] += 1
            if not uni:
                uni = temp
                continue

            for i in range(26):
                uni[i] = max(uni[i], temp[i])
        
        ans = []

        for word in words1:
            temp = [0] * 26
            for s in word:
                temp[ord(s) - ord('a')] += 1
            for c1, c2 in zip(temp, uni):
                if c2 > c1:
                    break
            else:
                ans.append(word)
        return ans


           

        # get lcm for w2