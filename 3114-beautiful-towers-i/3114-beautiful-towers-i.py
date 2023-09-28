class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:

        N = len(maxHeights)
        forward = []
        backward = []
        stack = []
        prev = maxHeights[0]
        index = None
    
        for i,h in enumerate(maxHeights):
           
            if h >= prev:
                if not forward:
                    forward.append(h)
                else:
                    forward.append(h + forward[-1])
                prev = h
                stack.append((h,i))
                continue
            # print(i, stack)
            while h < prev:
                if not stack:
                    prev = h
                    index = None
                    break
                prev, index = stack.pop()
            # print(i, 'after', prev, h, index)
            if index is not None:
                # print('has index',i,index, prev, h,h*(i-index),forward[index] )
                stack.append((prev,index))
                forward.append(h*(i-index) + forward[index])
            else:
                forward.append(h*(i+1))
            prev = h
            stack.append((h,i))

        stack = []
        prev = maxHeights[-1]
        index = None
        for i,h in enumerate(maxHeights[::-1]):
           
            if h >= prev:
                if not backward:
                    backward.append(h)
                else:
                    backward.append(h + backward[-1])
                prev = h
                stack.append((h,i))
                continue

            while h < prev:
                if not stack:
                    prev = h
                    index = None
                    break
                prev, index = stack.pop()
            
            if index is not None:
                stack.append((prev,index))
                backward.append(h*(i-index) + backward[index])
            else:
                backward.append(h*(i+1))
            prev = h
            stack.append((h,i))

     
        # forward[0] = 0
        # backward.append(0)
        backward.reverse()
        print(forward, backward)

        maxSum = forward[-1]
    
        for i in range(N):
            if i== 0:
                maxSum = max(maxSum,backward[i])

            else:
                maxSum = max(maxSum,forward[i-1] + backward[i])

        return maxSum
            
        