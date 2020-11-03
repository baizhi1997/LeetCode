
# @Title: 验证外星语词典 (Verifying an Alien Dictionary)
# @Author: qinxinlei
# @Date: 2018-12-14 15:52:49
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        return sorted(words, key=lambda x: [order.index(i) for i in x]) == words
