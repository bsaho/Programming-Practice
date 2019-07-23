import random


class Codec:
    def __init__(self):
        self.urlDict= dict ()

    def encode(self, longUrl):
        charRange= []
        tinyStr =""
        charRange.extend (range (ord("a"),ord("z")+1))
        charRange.extend (range (ord("A"),ord("Z")+1))
        charRange.extend (range (ord("0"), ord("9")+1))
        for i in range (0,6):
            randVal= random.randint(0,len (charRange)-1)
            tinyStr= tinyStr + chr (charRange[randVal])
        print (tinyStr)

        self.urlDict[tinyStr]= longUrl
        return tinyStr
        # print (self.urlDict[tinyStr])
        
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        if shortUrl in self.urlDict:
            print (self.urlDict.get (shortUrl))
            return self.urlDict.get (shortUrl)
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
# Your Codec object will be instantiated and called as such:
codec = Codec()
url="https://leetcode.com/problems/design-tinyurl"
codec.decode(codec.encode(url))

