class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dSet = set()
        for n in deadends:
            dSet.add(n)

        q = deque(["0000"])
        seen = set()
        steps = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node in seen or node in dSet:
                    continue
                seen.add(node)

                if node == target:
                    return steps 
                
                number = int(node)
                for i in range(4):
                    addVal = subVal = 10 ** i 
                    if int(node[3-i]) + 1 > 9:
                        addVal *= -9
                    if int(node[3-i]) - 1 < 0:
                        subVal *= -9
                    q.append(str(abs(number + addVal)).zfill(4))
                    q.append(str(abs(number - subVal)).zfill(4))
            steps += 1
        return -1
                

        return 0