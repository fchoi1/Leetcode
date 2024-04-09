class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        string = ''
        for char in s:
            dist = min(ord(char) - ord('a'),  ord('a') + 26 - ord(char))
            print("K", k,  dist)
            if dist <= k:
                string = string + 'a'
                k -= dist
            else:
                print(k, char, ord(char) - k, chr(ord(char) - k), string)
                string = string + chr(ord(char) - k)
                k = 0

        # adad k = 2
        # aaaai


        return string