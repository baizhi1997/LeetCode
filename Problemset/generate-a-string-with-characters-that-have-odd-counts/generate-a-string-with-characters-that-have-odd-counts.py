
# @Title: 生成每种字符都是奇数个的字符串 (Generate a String With Characters That Have Odd Counts)
# @Author: qinxinlei
# @Date: 2020-07-29 12:32:41
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def generateTheString(self, n: int) -> str:
        if n&1:
            return 'a'*n
        return 'a'*(n-1)+'b'
