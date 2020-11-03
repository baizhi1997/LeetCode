
# @Title: 根据字符出现频率排序 (Sort Characters By Frequency)
# @Author: qinxinlei
# @Date: 2018-11-28 21:09:23
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=collections.Counter(s)
        t=sorted(d.keys(),key=lambda c:-d[c])
        return ''.join(d[c]*c for c in t)
