
# @Title: 重复的DNA序列 (Repeated DNA Sequences)
# @Author: qinxinlei
# @Date: 2018-12-04 14:50:05
# @Runtime: 76 ms
# @Memory: N/A

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans=set()
        set1=set()
        for i in range(len(s)-9):
            t=s[i:i+10]
            if t in set1:
                ans.add(t)
            else:
                set1.add(t)
        return list(ans)
