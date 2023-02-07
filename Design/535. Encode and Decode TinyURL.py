class Codec:
    def __init__(self):
        self.table = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.id += 1
        self.table[self.id] = longUrl
        return "http://tinyurl.com/" + str(self.id)  # return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        i = shortUrl.rfind('/')  # from right to left, find index of "/"
        idx = int(shortUrl[i + 1:])  # find ID after "/"
        return self.table[idx]

    # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))