
# @Title: 逃脱阻碍者 (Escape The Ghosts)
# @Author: qinxinlei
# @Date: 2018-12-10 16:29:06
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        d=abs(target[0])+abs(target[1])
        return all(d<abs(p[0]-target[0])+abs(p[1]-target[1]) for p in ghosts)
