class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        # adj grid
        friendMap = defaultdict(set)

        # get k level friends
        seen = set([id])
        q = deque([id])
        for _ in range(level):
            for _ in range(len(q)):
                curr = q.popleft()
                for f in friends[curr]:
                    if f not in seen:
                        seen.add(f)
                        q.append(f)
        print(q)
        counts = defaultdict(int)
        for friend in q:
            for vids in watchedVideos[friend]:
                counts[vids] += 1
        # items = sorted(counts.items(), key=lambda x: (x[1], x[0]))
        # print(items)
        return [x[0] for x in sorted(counts.items(), key=lambda x: (x[1], x[0]))]

