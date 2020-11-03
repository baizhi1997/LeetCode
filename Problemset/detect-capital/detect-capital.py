
# @Title: 检测大写字母 (Detect Capital)
# @Author: qinxinlei
# @Date: 2018-10-22 15:06:12
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
