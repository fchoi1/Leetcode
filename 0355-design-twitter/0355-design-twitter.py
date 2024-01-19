from collections import defaultdict
import heapq 

class Twitter:

    def __init__(self):
        self.userList = defaultdict(set)
        self.userNews = defaultdict(list)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.userNews[userId], (self.count,tweetId))
        self.count += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.userList[userId]
        following.add(userId)
        userFeeds = []
        for user in following:
            feed = heapq.nlargest(10, self.userNews[user])
            userFeeds += feed
        heapq.heapify(userFeeds)
        return [x[1] for x in heapq.nlargest(10, userFeeds)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userList[followerId].discard(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)