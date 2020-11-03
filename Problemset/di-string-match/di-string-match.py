
# @Title: 增减字符串匹配 (DI String Match)
# @Author: qinxinlei
# @Date: 2018-11-18 18:37:11
# @Runtime: 108 ms
# @Memory: N/A

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l=0
        r=len(S)
        ans=[]
        for c in S:
            if c=='I':
                ans.append(l)
                l+=1
            else:
                ans.append(r)
                r-=1
        ans.append(l)
        return ans
