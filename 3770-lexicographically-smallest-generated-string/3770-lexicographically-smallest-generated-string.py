class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        size = n + m - 1

        res = ['?'] * size
        locked = [False] * size  # tracks positions fixed by 'T'

        # Step 1: Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if res[idx] == '?' or res[idx] == str2[j]:
                        res[idx] = str2[j]
                        locked[idx] = True
                    else:
                        return ""

        # Step 2: Fill remaining with 'a'
        for i in range(size):
            if res[i] == '?':
                res[i] = 'a'

        # Step 3: Handle 'F'
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(res[i:i+m]) == str2:
                    changed = False

                    # Try to break using an *unlocked* position
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        if not locked[idx]:
                            for c in range(26):
                                ch = chr(ord('a') + c)
                                if ch != str2[j]:
                                    res[idx] = ch
                                    changed = True
                                    break
                        if changed:
                            break

                    if not changed:
                        return ""

        return ''.join(res)