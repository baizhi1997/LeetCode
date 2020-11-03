
# @Title: 划分字母区间 (Partition Labels)
# @Author: qinxinlei
# @Date: 2018-11-21 20:30:45
# @Runtime: 88 ms
# @Memory: N/A

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic={}
        for i,c in enumerate(S):
            dic[c]=i
        ans=[]
        start=-1
        end=0
        for i,c in enumerate(S):
            if end<dic[c]:
                end=dic[c]
            if end==i:
                ans.append(end-start)
                start=i
        return ans
