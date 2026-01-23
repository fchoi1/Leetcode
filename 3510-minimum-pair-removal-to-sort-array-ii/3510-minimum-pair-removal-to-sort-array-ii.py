class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # heap + map?

        # count index that needs to be removed/udpated

        # store sums of i, i + 1 -> key: (i)  val = nums[i] + nums[i+1]
        # store a map 

        # use a map to store the next and prev index

        # get lowest and we delete map[i + 1] 
        # update map[i] with  lowest + nums[i + times update]
        # push into heap


        N = len(nums)
        linked = { N - 1: (N - 2, None) } # idx:  (prevIdx, currIdx)
        heap = []
        remove = set()

        for i, (prev, curr) in enumerate(zip(nums, nums[1:])):

            # construct linked
            if i == 0:
                linked[i] = (None, i + 1)
            else:
                linked[i] = (i - 1, i + 1)
            
            # construct index to remove
            if curr < prev:
                remove.add(i)

            # construct heap
            heappush(heap, (prev + curr, i))

        # if len(remove) == 0:
        #     return 0


        ops = 0
        while heap and len(remove) > 0:
      
            lowest, idx = heappop(heap)
            prevIdx, nextIdx = linked[idx]

            # already removed
            if nums[idx] == None:
                continue

            # check is entry is valid:
            if nextIdx != None:
                if lowest != nums[idx] + nums[nextIdx]:
                    continue
            else:
                continue

            remove.discard(idx)
            
            ops += 1

            # update idx
            nums[idx] = lowest

            # add new prev to heap
            if prevIdx != None:
                
                # update prev link
                prevPrevIdx, prevNextIdx = linked[prevIdx]
                linked[prevIdx] = (prevPrevIdx, idx)
                if nums[prevIdx] > lowest:
                    remove.add(prevIdx)
                else:
                    remove.discard(prevIdx)

                heappush(heap, (nums[prevIdx] + lowest, prevIdx))
            
            if nextIdx != None:
                # remove nextIdx
                nums[nextIdx] = None
                remove.discard(nextIdx)

                # update curr link
                _, nextNextIdx = linked[nextIdx]
                linked[idx] = (prevIdx, nextNextIdx)

                # update future link
                if nextNextIdx != None:
                    linked[nextNextIdx] = (idx, linked[nextNextIdx][1])
                
                    if lowest > nums[nextNextIdx]:
                        remove.add(idx)

                    heappush(heap, (lowest +  nums[nextNextIdx], idx))
        return ops 
            

            
      
            