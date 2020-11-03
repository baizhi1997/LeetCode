
# @Title: 寻找比目标字母大的最小字母 (Find Smallest Letter Greater Than Target)
# @Author: qinxinlei
# @Date: 2018-11-02 21:52:49
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        return letters[bisect.bisect_right(letters,target)%len(letters)]
