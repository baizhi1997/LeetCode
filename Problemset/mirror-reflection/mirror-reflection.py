
# @Title: 镜面反射 (Mirror Reflection)
# @Author: qinxinlei
# @Date: 2018-11-23 20:45:39
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        if p&1 and q&1:
            return 1
        if p&1:
            return 0
        if q&1:
            return 2
        return self.mirrorReflection(p//2,q//2)
