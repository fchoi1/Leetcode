class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyMap = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for char in key:
            if char == " " or char in keyMap:
                continue
            keyMap[char] = alpha[i]
            i += 1
            if i == 26:
                break
        m = ""
        for char in message:
            if char == " ":
                m += " "
            else:
                m += keyMap[char]
        return m
        