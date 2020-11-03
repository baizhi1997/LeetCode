
# @Title: 重复叠加字符串匹配 (Repeated String Match)
# @Author: qinxinlei
# @Date: 2018-11-17 20:58:33
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if set(A)!=set(B) and len(A)<=len(B):
            return -1
        i=math.ceil(len(B)/len(A))
        if B in A*i:
            return i
        if B in A*(i+1):
            return i+1
        return -1
