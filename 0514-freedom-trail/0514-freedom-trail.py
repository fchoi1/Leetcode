class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Helper function to get next closest index
        def rotate(direction, node, steps, index):
            while ring[node] != key[index]:
                node += 1 if direction == "cw" else -1
                if node < 0:
                    node += len(ring)
                elif node >= len(ring):
                    node -= len(ring)
                steps += 1
            return node, steps

        q = deque([(0,0)])
        wordLen = 0 
        while q:
            lowest = [float('inf') for _ in range(len(ring))]
            for _ in range(len(q)):
                node, currStep = q.popleft()

                # Get next left and right index and steps taken
                left,leftStep = rotate("cw", node, currStep, wordLen)
                right,rightStep = rotate("ccw", node, currStep, wordLen)

                # Update lowest value from left and right
                lowest[left] = min(lowest[left], leftStep + 1)
                lowest[right] = min(lowest[right], rightStep + 1)
                
            wordLen += 1
            # check after wordlen is reached
            if wordLen == len(key):
                return min(lowest)

            # populate indexes that have a the lowest value only
            for i,val in enumerate(lowest):
                if val != float('inf'):
                    q.append((i, val))