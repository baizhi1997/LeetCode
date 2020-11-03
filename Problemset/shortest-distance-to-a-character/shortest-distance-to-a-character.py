
# @Title: 字符的最短距离 (Shortest Distance to a Character)
# @Author: qinxinlei
# @Date: 2018-10-20 13:07:50
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ans=[]
        i=float('inf')
        for s in S:
            if s==C:
                i=0
            ans.append(i)
            i+=1
        i=float('inf')
        j=len(S)-1
        for s in S[::-1]:
            if s==C:
                i=0
            ans[j]=min(ans[j],i)
            j-=1
            i+=1
        return ans
