class Codec:
    # Runtime: 12 ms
    # Memory: 13.3 MB
    count = -1
    hashmap = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        self.hashmap[self.count] = longUrl
        return "https://example.com/" + str(self.count)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.hashmap[int(shortUrl.lstrip("https://example.com/"))]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
