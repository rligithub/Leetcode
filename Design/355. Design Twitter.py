class Twitter:

    def __init__(self):
        self.tweets = collections.defaultdict(list)  # {userId: (order, tweetID)}
        self.following = collections.defaultdict(set)  # {user1: (user2, user3)}
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] += (self.order, tweetId),
        self.order -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for user in self.following[userId] | {userId}:
            for tw in self.tweets[user]:
                res.append(tw)
        res = sorted(res)[:10]

        ans = []
        for i, news in res:
            ans.append(news)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)