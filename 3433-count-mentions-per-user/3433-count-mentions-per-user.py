class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        
        ans = []
        status = {str(i):-1 for i in range(numberOfUsers)}
        mentions = [0 for _ in range(numberOfUsers)]
        events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])))

        def checkOffline(time):
            for k,v in status.items():
                if int(time) >= v:
                    status[k] = -1
        
        def getOnline(time):
            ids = []
            for k,v in status.items():
                if v <= int(time):
                    ids.append(int(k))
            return ids

        print(events)
        for action, time, mention in events:
            t = int(time)
            checkOffline(time)

            if action == "OFFLINE":
                status[mention] = t + 60
            else:
                if mention == "HERE":
                    for i in getOnline(time):
                        mentions[i] += 1
                elif mention == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                else:
                    # parse ids
                    for idStr in mention.split(" "):
                        i = int(idStr[2:])
                        mentions[i] += 1

        return mentions