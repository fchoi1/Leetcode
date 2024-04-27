class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.steps = float('inf')

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

                left,leftStep = rotate("cw", node, currStep, wordLen)
                right,rightStep = rotate("ccw", node, currStep, wordLen)
                lowest[left] = min(lowest[left], leftStep + 1)
                lowest[right] = min(lowest[right], rightStep + 1)
            wordLen += 1
            if wordLen == len(key):
                return min(lowest)
            for i,val in enumerate(lowest):
                if val != float('inf'):
                    q.append((i, val))

        seen = {}
        def traverse(node, currStep, wordLen):
            if currStep >= self.steps:
                return        
            if (node, wordLen) in seen:
                if currStep >= seen[(node,wordLen)]:
                    return
            seen[(node, wordLen)] = currStep
            if wordLen == len(key):
                self.steps = min(self.steps, currStep)
                seen[(node, wordLen)] = self.steps
                return

            # cw
            left,leftStep = rotate("cw", node, currStep, wordLen)
            right,rightStep = rotate("ccw", node, currStep, wordLen)
            traverse(left, leftStep + 1, wordLen + 1)
            traverse(right, rightStep + 1, wordLen + 1)

        # traverse(0,0,0)
        # return self.steps