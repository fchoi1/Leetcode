class Solution:
    def compressedString(self, word: str) -> str:
        c = 1
        prev = word[0]
        string = ''
        for w in word[1:]:
            if w == prev:
                c += 1
                if c >= 9:
                    string += str(c) + prev
                    c = 0
            else:
                if c > 0:
                    string += str(c) + prev
                c = 1
            prev = w

        return string + str(c) + prev if c > 0 else string