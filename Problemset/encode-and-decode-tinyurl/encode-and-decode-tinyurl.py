
# @Title: TinyURL 的加密与解密 (Encode and Decode TinyURL)
# @Author: qinxinlei
# @Date: 2018-11-19 15:26:09
# @Runtime: 28 ms
# @Memory: N/A

class Codec:
    
    def __init__(self):
        self.dic = {}
        self.key = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.key += 1
        txt = 'tinyurl' + str(self.key)
        self.dic[txt] = longUrl
        return txt
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dic[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
