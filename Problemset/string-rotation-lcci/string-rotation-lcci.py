
# @Title: 字符串轮转 (String Rotation LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 11:51:49
# @Runtime: 56 ms
# @Memory: 13.4 MB

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return s2 in s1*2 and len(s1) == len(s2)
