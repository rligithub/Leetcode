# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        index = startUrl[7:].find('/')  # find index of first'/' in urls without "http://"

        hostname = startUrl[:index]

        visited = set()
        visited.add(startUrl)
        if len(htmlParser.getUrls(startUrl)) != 0:
            self.dfs(startUrl, htmlParser, hostname, visited)
        return list(visited)

    def dfs(self, startUrl, htmlParser, hostname, visited):
        if len(htmlParser.getUrls(startUrl)) == 0:
            return
        for nxtUrl in htmlParser.getUrls(startUrl):
            if hostname in nxtUrl and nxtUrl not in visited:
                visited.add(nxtUrl)
                self.dfs(nxtUrl, htmlParser, hostname, visited)
