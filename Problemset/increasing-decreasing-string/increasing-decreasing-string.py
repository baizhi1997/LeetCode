
# @Title: 上升下降字符串 (Increasing Decreasing String)
# @Author: qinxinlei
# @Date: 2020-07-29 10:58:25
# @Runtime: 108 ms
# @Memory: 13.5 MB

class Solution:
    def sortString(self, s: str) -> str:
        h = [0] * 26
        for ch in s:
            h[ord(ch) - 97] += 1

        def appendChar(ret, p):
            if h[p] > 0:
                h[p] -= 1
                ret.append(chr(p + 97))
        
        def haveChar():
            return any(h[i] > 0 for i in range(26))
        
        ret = list()
        while True:
            if not haveChar():
                break
            for i in range(26):
                appendChar(ret, i)
            for i in range(26):
                appendChar(ret, 25 - i)
        return "".join(ret)

