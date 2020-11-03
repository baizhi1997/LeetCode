
# @Title: 整理字符串 (Make The String Great)
# @Author: qinxinlei
# @Date: 2020-08-10 16:23:21
# @Runtime: 56 ms
# @Memory: 13.4 MB

class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ""
        i = 0
        tmp = ord('A') - ord('a')
        while i < len(s)-1:
            if ord(s[i])-ord(s[i+1])==tmp or ord(s[i+1])-ord(s[i])==tmp:
                s = s[:i] + s[i+2:]
                s = self.makeGood(s)
                break
            i += 1
        return s
