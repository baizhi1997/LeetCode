
# @Title: 在LR字符串中交换相邻字符 (Swap Adjacent in LR String)
# @Author: qinxinlei
# @Date: 2018-10-13 11:02:28
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        s1=[(c,i) for i,c in enumerate(start) if c=='L' or c=='R']
        s2=[(c,i) for i,c in enumerate(end) if c=='L' or c=='R']
        return len(s1)==len(s2) and all(c1==c2 and (i1>=i2 and c1=='L' or i1<=i2 and c1=='R') for (c1,i1),(c2,i2) in zip(s1,s2))
