
# @Title: 朋友圈 (Friend Circles)
# @Author: qinxinlei
# @Date: 2018-12-13 15:16:22
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        set1=set()
        ans=0
        n=len(M)
        for j in range(n):
            if j in set1:
                continue
            tmp=[j]
            i=0
            while i<len(tmp):
                for k in range(n):
                    if M[tmp[i]][k]==1 and k not in tmp:
                        tmp.append(k)
                i+=1
            set1.update(tmp)
            ans+=1
        return ans
