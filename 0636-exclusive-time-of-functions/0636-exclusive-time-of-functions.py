class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:


        parsedLogs = []
        for s in logs:
            fId, action, time = s.split(':')
            
            heappush(parsedLogs, (int(time), int(fId), action == 'end'))
        
        total = [0 for _ in range(n)]
        stack = [] # fId, startTime
        print(parsedLogs)
        while len(parsedLogs) > 0:

            print(stack, "log", parsedLogs[0], total)
            time, fId, isEnd = heappop(parsedLogs)

            if not isEnd:
                if stack:
                    currId, currTime = stack[-1]
                    total[currId] += time - currTime
                stack.append((fId, time))
            else:
                # assumed the top of the stack
                currId, currTime = stack.pop()
                total[currId] += time - currTime + 1
                print("popping", currId, currTime, time, total)
                
                if stack:
                    stack[-1] = (stack[-1][0], time + 1)
        
        return total