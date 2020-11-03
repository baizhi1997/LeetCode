
# @Title: 赎金信 (Ransom Note)
# @Author: qinxinlei
# @Date: 2018-10-23 16:13:20
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic1=collections.Counter(ransomNote)
        dic2=collections.Counter(magazine)
        return not dic1-dic2
