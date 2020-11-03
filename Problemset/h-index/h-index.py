
# @Title: H 指数 (H-Index)
# @Author: qinxinlei
# @Date: 2018-12-04 15:15:10
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l=len(citations)
        tmp=[0]*(l+1)
        for c in citations:
            if c>=l:
                tmp[l]+=1
            else:
                tmp[c]+=1
        while l>0:
            if tmp[l]>=l:
                return l
            l-=1
            tmp[l]+=tmp[l+1]
        return 0
