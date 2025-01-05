class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        diff = [0] * (len(s) + 1)
        for start,end,d in shifts:
            diff[start] += 1 if d else -1
            diff[end + 1] -= 1 if d else -1

        string = ''
        currDiff = 0
        for char,d in zip(s,diff):
            currDiff += d
            i = ord(char) - ord('a') + currDiff
            string += chr(97 + i % 26)
        return string
        


        

        