
# @Title: URL化 (String to URL LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 14:19:07
# @Runtime: 56 ms
# @Memory: 18.8 MB

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')
