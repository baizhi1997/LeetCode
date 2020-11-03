
# @Title: 分发饼干 (Assign Cookies)
# @Author: qinxinlei
# @Date: 2018-11-14 16:19:14
# @Runtime: 72 ms
# @Memory: N/A

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        l=len(g)
        ans=0
        for x in s:
            if ans<l and x>=g[ans]:
                ans+=1
        return ans
