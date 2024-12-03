class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        sentance = ""
        currIndex = 0
        curr = spaces[currIndex]

        for i,char in enumerate(s):
            if i == curr:
                sentance += " "
                currIndex += 1
                curr = spaces[currIndex] if currIndex < len(spaces) else None
            sentance += char

        return sentance
        